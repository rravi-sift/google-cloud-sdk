# Copyright 2015 Google Inc. All Rights Reserved.

"""The gen-config command."""

import os

from googlecloudsdk.calliope import base
from googlecloudsdk.core import log
from googlecloudsdk.core import properties

from googlecloudsdk.appengine.lib import fingerprinting
from googlecloudsdk.appengine.lib import yaml_parsing
from googlecloudsdk.appengine.lib.runtimes import fingerprinter


class GenConfig(base.Command):
  """Generate missing configuration files for a source directory.

  This command generates all relevant config files (app.yaml, Dockerfile and a
  build Dockerfile) for your application in the current directory or emits an
  error message if the source directory contents are not recognized.
  """

  detailed_help = {
      'DESCRIPTION': '{description}',
      'EXAMPLES': """\
          To generate configs for the current directory:

            $ {command}

          To generate configs for ~/my_app:

            $ {command} ~/my_app
          """
  }

  @staticmethod
  def Args(parser):
    parser.add_argument(
        'source_dir',
        nargs='?',
        help='The source directory to fingerprint.',
        default=os.getcwd())
    parser.add_argument(
        '--config',
        default=None,
        help=('The yaml file defining the module configuration.  This is '
              'normally one of the generated files, but when generating a '
              'custom runtime there can be an app.yaml containing parameters.'))
    parser.add_argument(
        '--custom',
        action='store_true',
        default=False,
        help=('If true, generate config files for a custom runtime.  This '
              'will produce a Dockerfile, a .dockerignore file and an app.yaml '
              '(possibly other files as well, depending on the runtime).'))

  def Run(self, args):
    if args.config:
      # If the user has specified an config file, use that.
      config_filename = args.config
    else:
      # Otherwise, check for an app.yaml in the source directory.
      config_filename = os.path.join(args.source_dir, 'app.yaml')
      if not os.path.exists(config_filename):
        config_filename = None

    # If there was an config file either specified by the user or in the source
    # directory, load it.
    if config_filename:
      try:
        project = properties.VALUES.core.project.Get(required=True)
        myi = yaml_parsing.ModuleYamlInfo.FromFile(config_filename,
                                                   project,
                                                   version=None,
                                                   check_version=False)
        config = myi.parsed
      except IOError as ex:
        log.error('Unable to open %s: %s', config_filename, ex)
        return
    else:
      config = None

    fingerprinter.GenerateConfigs(
        args.source_dir,
        fingerprinting.Params(appinfo=config, custom=args.custom))
