# Copyright 2015 Google Inc. All Rights Reserved.
#!/usr/bin/python2.4
#
# Copyright 2010 Google Inc. All Rights Reserved.

"""Repository for all builtin handlers information.

On initialization, this file generates a list of builtin handlers that have
associated app.yaml information.  This file can then be called to read that
information and make it available.
"""

# WARNING: This file is externally viewable by our users.  All comments from
# this file will be stripped.  The docstrings will NOT.  Do not put sensitive
# information in docstrings.  If you must communicate internal information in
# this source file, please place them in comments only.

# To add a new builtin handler definition:
# - create a new directory in apphosting/ext/builtins/foo
# - modify the apphosting/ext/builtins/BUILD file and include your new
#   include.yaml and include-python27.yaml files in the INCLUDE_YAML_FILES
#   constant



import logging
import os

# Absolute path of directory file is contained in.  Builtins should be in
# subdirectories of this directory.
DEFAULT_DIR = os.path.join(os.path.dirname(__file__))
_handler_dir = None

# Initialized on load with names of all subdirectories which contain
# app.yaml files.
_available_builtins = None
BUILTINS_NOT_AVAIABLE_IN_PYTHON27 = set(['datastore_admin', 'mapreduce'])

# Default name for builtin handlers configuration files.
INCLUDE_FILENAME_TEMPLATE = 'include-%s.yaml'
DEFAULT_INCLUDE_FILENAME = 'include.yaml'


class InvalidBuiltinName(Exception):
  """Raised whenever a builtin handler name is specified that is not found."""


def reset_builtins_dir():
  """Public method for resetting builtins directory to default."""
  set_builtins_dir(DEFAULT_DIR)


def set_builtins_dir(path):
  """Sets the appropriate path for testing and reinitializes the module."""
  global _handler_dir, _available_builtins
  _handler_dir = path
  _available_builtins = []
  _initialize_builtins()


def _initialize_builtins():
  """Scan the immediate subdirectories of the builtins module.

  Encountered subdirectories with an app.yaml file are added to
  AVAILABLE_BUILTINS.
  """
  if os.path.isdir(_handler_dir):
    for filename in os.listdir(_handler_dir):
      if os.path.isfile(_get_yaml_path(filename, '')):
        _available_builtins.append(filename)


def _get_yaml_path(builtin_name, runtime):
  """Return expected path to a builtin handler's yaml file without error check.
  """
  runtime_specific = os.path.join(_handler_dir, builtin_name,
                                  INCLUDE_FILENAME_TEMPLATE % runtime)
  if runtime and os.path.exists(runtime_specific):
    return runtime_specific
  return os.path.join(_handler_dir, builtin_name, DEFAULT_INCLUDE_FILENAME)


def get_yaml_path(builtin_name, runtime=''):
  """Returns the full path to a yaml file by giving the builtin module's name.

  Args:
    builtin_name: single word name of builtin handler
    runtime: name of the runtime

  Raises:
    ValueError: if handler does not exist in expected directory

  Returns:
    the absolute path to a valid builtin handler include.yaml file
  """
  if _handler_dir is None:
    set_builtins_dir(DEFAULT_DIR)

  available_builtins = set(_available_builtins)
  if runtime == 'python27':
    available_builtins = available_builtins - BUILTINS_NOT_AVAIABLE_IN_PYTHON27

  if builtin_name not in available_builtins:
    raise InvalidBuiltinName(
        '%s is not the name of a valid builtin.\n'
        'Available handlers are: %s' % (
            builtin_name, ', '.join(sorted(available_builtins))))
  return _get_yaml_path(builtin_name, runtime)


# Needed by codesite.appengine.launchy.fake_os_path and
# codesite.appengine.launchy.appcfg_patch
def get_yaml_basepath():
  """Returns the full path of the directory in which builtins are located."""
  if _handler_dir is None:
    set_builtins_dir(DEFAULT_DIR)
  return _handler_dir
