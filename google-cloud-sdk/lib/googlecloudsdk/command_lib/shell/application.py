# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The gcloud shell prompt_toolkit application."""

from __future__ import unicode_literals

import subprocess
import sys

from googlecloudsdk.command_lib.shell import browser
from googlecloudsdk.command_lib.shell import completer as shell_completer
from googlecloudsdk.command_lib.shell import gcloud_parser
from googlecloudsdk.command_lib.shell import layout
from googlecloudsdk.command_lib.shell import style as shell_style
from googlecloudsdk.core import properties
from googlecloudsdk.core.configurations import named_configs
from prompt_toolkit import application
from prompt_toolkit import buffer as pt_buffer
from prompt_toolkit import document
from prompt_toolkit import filters
from prompt_toolkit import history as pt_history
from prompt_toolkit import interface
from prompt_toolkit import keys
from prompt_toolkit import shortcuts
from prompt_toolkit.key_binding import manager
from prompt_toolkit.token import Token

try:
  from prompt_toolkit.terminal import win32_input as terminal_input  # pylint: disable=g-import-not-at-top
except ImportError:
  from prompt_toolkit.terminal import vt100_input as terminal_input  # pylint: disable=g-import-not-at-top


# TODO(b/35347247): deglobalize ShowHelpWindow
# This variable is changed at runtime and determines whether or not the help bar
# should be shown.
SHOW_HELP_WINDOW = True


def CreateKeyBindingRegistry():
  """Configures the keybindings for the shell."""
  def _HandleCtrlQ(event):
    event.cli.set_return_value(None)

  def _HandleCtrlH(_):
    global SHOW_HELP_WINDOW
    SHOW_HELP_WINDOW = not SHOW_HELP_WINDOW

  def _HandleCtrlV(event):
    doc = event.cli.current_buffer.document
    browser.OpenReferencePage(doc.text, doc.cursor_position)

  m = manager.KeyBindingManager(
      enable_abort_and_exit_bindings=True,
      enable_system_bindings=True,
      enable_search=True,
      enable_auto_suggest_bindings=True,)

  ControlHHack(m.registry)
  m.registry.add_binding(keys.Keys.ControlQ, eager=True)(_HandleCtrlQ)
  m.registry.add_binding(keys.Keys.ControlH, eager=True)(_HandleCtrlH)
  m.registry.add_binding(keys.Keys.ControlV, eager=True)(_HandleCtrlV)

  return m.registry


# TODO(b/35347443): update prompt toolkit to make this unnecessary.
def ControlHHack(registry):
  """A bad hack to make ctrl+h work.

  This code is based on the fix for
  https://github.com/jonathanslenders/pymux/issues/50. Control H and backspace
  are considered the same key. This means that if you bind Control H, backspace
  will cease to function. This function monkey patches prompt toolkit to
  consider '<Backspace>' separate from Control H and then adds a binding on
  backspace so it deletes the previous character in the current buffer.

  Args:
    registry: a prompt_toolkit key binding Registry
  """
  terminal_input.ANSI_SEQUENCES['\x7f'] = '<Backspace>'

  insert_mode = filters.ViInsertMode() | filters.EmacsInsertMode()
  @registry.add_binding('<Backspace>', filter=insert_mode)
  def _HandleBackspace(event):
    """Backspace: delete before cursor."""
    deleted = event.current_buffer.delete_before_cursor(count=event.arg)
    if not deleted:
      event.cli.output.bell()

    registry.add_binding('<Backspace>', filter=insert_mode)(_HandleBackspace)


def GetBottomToolbarTokens(_):
  # Prevents caching of properties, so we will update the toolbar in response to
  # changes in property status
  named_configs.ActivePropertiesFile().Invalidate()
  project = properties.VALUES.core.project.Get() or '<NO PROJECT SET>'
  account = properties.VALUES.core.account.Get() or '<NO ACCOUNT SET>'
  return [
      (Token.Toolbar.Account, account),
      (Token.Toolbar.Separator, ' | '),
      (Token.Toolbar.Project, project),
      (Token.Toolbar.Separator, ' | '),
      (Token.Toolbar.Help, 'ctrl-q: Quit'),
      (Token.Toolbar.Separator, ' | '),
      (Token.Toolbar.Help, 'ctrl-h: Toggle Help'),
  ]


def GetCurrentToken(tokens, pos):
  """Determine the current token given a cursor position.

  Args:
    tokens: a list of gcloud_parser.ArgTokens
    pos: an int giving the current cursor position

  Returns:
    The gcloud_parser.ArgToken at that position or None.
  """
  i = 0
  while i < len(tokens):
    if pos > tokens[i].start and pos < tokens[i].end:
      return tokens[i]
    if pos < tokens[i].start:
      return tokens[i-1] if i > 0 else None
    i += 1

  return tokens[len(tokens)-1] if tokens else None


def GetHelpTokens(cli):
  doc = cli.current_buffer.document
  tok = GetCurrentToken(gcloud_parser.ParseLine(doc.text), doc.cursor_position)
  if tok is None:
    return []

  return [(Token.HelpToolbar.SectionName, 'Description: '),
          (Token.HelpToolbar.SectionValue, tok.tree['description'])]


def Prompt(history):
  """Show the shell prompt to the user."""
  app = CreatePromptApplication(
      'gcloud> ',
      get_bottom_toolbar_tokens=GetBottomToolbarTokens,
      style=shell_style.GetDocumentStyle(),
      key_bindings_registry=CreateKeyBindingRegistry(),
      get_help_tokens=GetHelpTokens,
      completer=shell_completer.ShellCliCompleter(),
      history=history)

  return RunApplication(app)


def RunApplication(app):
  """Run a prompt_toolkit Application."""

  eventloop = shortcuts.create_eventloop()

  # Create CommandLineInterface.
  cli = interface.CommandLineInterface(
      application=app, eventloop=eventloop, output=shortcuts.create_output())

  # Note: We pass `reset_current_buffer=False`, because that way it's easy to
  #       give DEFAULT_BUFFER a default value, without it getting erased. We
  #       don't have to reset anyway, because this is the first and only time
  #       that this CommandLineInterface will run.
  try:
    result = cli.run(reset_current_buffer=False)

    if isinstance(result, document.Document):  # Backwards-compatibility.
      return result.text
    return result
  finally:
    eventloop.close()


def CreatePromptApplication(
    message='',
    multiline=False,
    wrap_lines=True,
    is_password=False,
    complete_while_typing=True,
    enable_history_search=False,
    lexer=None,
    enable_system_bindings=False,
    enable_open_in_editor=False,
    validator=None,
    completer=None,
    reserve_space_for_menu=5,
    auto_suggest=None,
    style=None,
    history=None,
    clipboard=None,
    get_prompt_tokens=None,
    get_continuation_tokens=None,
    get_bottom_toolbar_tokens=None,
    display_completions_in_columns=False,
    get_title=None,
    mouse_support=False,
    extra_input_processors=None,
    key_bindings_registry=None,
    on_abort=application.AbortAction.RAISE_EXCEPTION,
    on_exit=application.AbortAction.RAISE_EXCEPTION,
    accept_action=pt_buffer.AcceptAction.RETURN_DOCUMENT,
    erase_when_done=False,
    default='',
    get_help_tokens=None):
  """Create the shell prompt Application."""
  if key_bindings_registry is None:
    key_bindings_registry = manager.KeyBindingManager.for_prompt(
        enable_system_bindings=enable_system_bindings,
        enable_open_in_editor=enable_open_in_editor).registry

  # Make sure that complete_while_typing is disabled when enable_history_search
  # is enabled. (First convert to SimpleFilter, to avoid doing bitwise
  # operations on bool objects.)
  complete_while_typing = shortcuts.to_simple_filter(complete_while_typing)
  enable_history_search = shortcuts.to_simple_filter(enable_history_search)
  multiline = shortcuts.to_simple_filter(multiline)

  complete_while_typing &= ~enable_history_search

  # Create application
  return application.Application(
      layout=layout.CreatePromptLayout(
          message=message,
          lexer=lexer,
          is_password=is_password,
          reserve_space_for_menu=(reserve_space_for_menu
                                  if completer is not None else 0),
          multiline=filters.Condition(lambda cli: multiline()),
          get_prompt_tokens=get_prompt_tokens,
          get_continuation_tokens=get_continuation_tokens,
          get_bottom_toolbar_tokens=get_bottom_toolbar_tokens,
          display_completions_in_columns=display_completions_in_columns,
          extra_input_processors=extra_input_processors,
          wrap_lines=wrap_lines,
          get_help_tokens=get_help_tokens,
          show_help=filters.Condition(lambda _: SHOW_HELP_WINDOW)),
      buffer=pt_buffer.Buffer(
          enable_history_search=enable_history_search,
          complete_while_typing=complete_while_typing,
          is_multiline=multiline,
          history=(history or pt_history.InMemoryHistory()),
          validator=validator,
          completer=completer,
          auto_suggest=auto_suggest,
          accept_action=accept_action,
          initial_document=document.Document(default),),
      style=style,
      clipboard=clipboard,
      key_bindings_registry=key_bindings_registry,
      get_title=get_title,
      mouse_support=mouse_support,
      erase_when_done=erase_when_done,
      on_abort=on_abort,
      on_exit=on_exit)


def FixControlQ():
  """Allow ctrl-q to be passed to the application on unix systems.

  Control+Q is usually used to unpause the terminal after Control+S pauses it on
  unix systems. To prevent this, we need to disable the termios.IXON flag.
  termios is not available on all platforms.

  Returns:
    A callable to reset the terminal to its original state. The callable takes
    no arguments.
  """
  # by default, no change was made so reset is a no-op.
  reset_tty = lambda: None

  try:
    import termios  # pylint: disable=g-import-not-at-top
    original_tty = termios.tcgetattr(0)
    new_tty = termios.tcgetattr(0)
    new_tty[0] &= ~termios.IXON
    termios.tcsetattr(0, termios.TCSANOW, new_tty)
    reset_tty = lambda: termios.tcsetattr(0, termios.TCSANOW, original_tty)
  except ImportError:
    pass

  return reset_tty


def main():
  reset_tty = FixControlQ()

  try:
    hist = pt_history.InMemoryHistory()

    while True:
      try:
        text = Prompt(hist)
        if text is None or text.strip() == 'exit':
          sys.exit(0)
        subprocess.call('gcloud ' + text, shell=True)
      except EOFError:
        # on ctrl-d, exit loop
        break
      except KeyboardInterrupt:
        # ignore ctrl-c
        pass
  finally:
    # when exitting, restore the tty to its original state.
    reset_tty()
