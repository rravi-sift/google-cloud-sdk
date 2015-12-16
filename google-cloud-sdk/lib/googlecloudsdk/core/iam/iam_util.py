# Copyright 2015 Google Inc. All Rights Reserved.
"""General IAM utilities used by the Cloud SDK."""

from googlecloudsdk.core import exceptions
from googlecloudsdk.third_party.apitools.base.protorpclite.messages import DecodeError
from googlecloudsdk.third_party.apitools.base.py import encoding


def AddArgsForAddIamPolicyBinding(parser):
  """Adds the IAM policy binding arguments for role and members.

  Args:
    parser: An argparse.ArgumentParser-like object to which we add the argss.

  Raises:
    ArgumentError if one of the arguments is already defined in the parser.
  """
  parser.add_argument(
      '--role', required=True,
      help='Define the role of the member')
  parser.add_argument(
      '--member', required=True,
      help='The member to add to the binding.')

def AddArgsForRemoveIamPolicyBinding(parser):
  """Adds the IAM policy binding arguments for role and members.

  Args:
    parser: An argparse.ArgumentParser-like object to which we add the argss.

  Raises:
    ArgumentError if one of the arguments is already defined in the parser.
  """
  parser.add_argument(
      '--role', required=True,
      help='The role to remove the member from')
  parser.add_argument(
      '--member', required=True,
      help='The member to remove from the binding.')


def AddBindingToIamPolicy(messages, policy, args):
  """Given an IAM policy, add new bindings as specified by args.

  An IAM binding is a pair of role and member. Check if the arguments passed
  define both the role and member attribute, create a binding out of their
  values, and append it to the policy.

  Args:
    messages: ToolResults API message classes generated by apitools.
        Required to create new bindings of the proper type.
    policy: IAM policy to which we want to add the bindings.
    args: argparse.Namespace, An object that contains the values for the
        arguments of a Cloud SDK command, including the arguments added by
        AddArgsForAddIamPolicyBinding.
  """
  if not hasattr(args, 'role') or not hasattr(args, 'member'):
    return

  # Just add the new binding at the end. Doesn't matter if there's already
  # a binding for the same role.
  policy.bindings.append(messages.Binding(
      members=[args.member],
      role='roles/{0}'.format(args.role)))


def RemoveBindingFromIamPolicy(policy, args):
  """Given an IAM policy, add remove bindings as specified by the args.

  An IAM binding is a pair of role and member. Check if the arguments passed
  define both the role and member attribute, search the policy for a binding
  that contains this role and member, and remove it from the policy.

  Args:
    policy: IAM policy from which we want to remove bindings.
    args: Arguments from the command line that contain possible values for
        keys added by AddArgsForAddIamPolicyBinding. This is what defines what
        bindings we remove.
  """
  if not hasattr(args, 'role') or not hasattr(args, 'member'):
    return

  for binding in policy.bindings:
    if (binding.role == 'roles/{0}'.format(args.role) and
        args.member in binding.members):
      binding.members.remove(args.member)
  # It's ok if some bindings have 0 members. The server should filter them out.


def ParseJsonPolicyFile(policy_file_path, policy_message_type):
  """Construct an IAM Policy protorpc.Message from a JSON formated file.

  Args:
    policy_file_path: Path to the JSON IAM policy file.
    policy_message_type: Policy message type to convert JSON to.
  Returns:
    a protorpc.Message of type policy_message_type filled in from the JSON
    policy file.
  Raises:
    BadFileException if the JSON file is malformed or does not exist.
  """
  try:
    with open(policy_file_path) as policy_file:
      policy_json = policy_file.read()
  except EnvironmentError:
    # EnvironmnetError is parent of IOError, OSError and WindowsError.
    # Raised when file does not exist or can't be opened/read.
    raise exceptions.Error(
        'Unable to read policy file {0}'.format(policy_file_path))

  try:
    policy = encoding.JsonToMessage(policy_message_type, policy_json)
  except (ValueError, DecodeError) as e:
    # ValueError is raised when JSON is badly formatted
    # DecodeError is raised when etag is badly formatted (not proper Base64)
    raise exceptions.Error(
        'Policy file {0} is not a properly formatted JSON policy file. {1}'
        .format(policy_file_path, str(e)))
  return policy

def GetDetailedHelpForSetIamPolicy(collection, example_id):
  """Returns a detailed_help for a set-iam-policy command

  Args:
    collection: Name of the command collection (ex: "project", "dataset")
    example_id: Collection identifier to display in a sample command
        (ex: "my-project", '1234')
  Returns:
    a dict with boilerplate help text for the set-iam-policy command
  """
  return {
      'brief': 'Set IAM policy for a {0}.'.format(collection),
      'DESCRIPTION': '{description}',
      'EXAMPLES': """\
          The following command will read an IAM policy defined in a JSON file
          'policy.json' and set it for a {0} with identifier '{1}'

            $ {{command}} {1} policy.json

          See https://cloud.google.com/iam/docs/managing-policies for details
          of the policy file format and contents.
          """.format(collection, example_id)
  }


def GetDetailedHelpForAddIamPolicyBinding(collection, example_id):
  """Returns a detailed_help for an add-iam-policy-binding command

  Args:
    collection: Name of the command collection (ex: "project", "dataset")
    example_id: Collection identifier to display in a sample command
        (ex: "my-project", '1234')
  Returns:
    a dict with boilerplate help text for the add-iam-policy-binding command
  """
  return {
      'brief': 'Add IAM policy binding for a {0}.'.format(collection),
      'DESCRIPTION': '{description}',
      'EXAMPLES': """\
          The following command will add an IAM policy binding for the role
          of 'editor' for the user 'test-user@gmail.com' on a {0} with
          identifier '{1}'

            $ {{command}} {1} --editor='user:test-user@gmail.com'

          See https://cloud.google.com/iam/docs/managing-policies for details
          of policy role and member types.
          """.format(collection, example_id)
  }

def GetDetailedHelpForRemoveIamPolicyBinding(collection, example_id):
  """Returns a detailed_help for a remove-iam-policy-binding command

  Args:
    collection: Name of the command collection (ex: "project", "dataset")
    example_id: Collection identifier to display in a sample command
        (ex: "my-project", '1234')
  Returns:
    a dict with boilerplate help text for the remove-iam-policy-binding command
  """
  return {
      'brief': 'Remove IAM policy binding for a {0}.'.format(collection),
      'DESCRIPTION': '{description}',
      'EXAMPLES': """\
          The following command will remove a IAM policy binding for the role
          of 'editor' for the user 'test-user@gmail.com' on {0} with
          identifier '{1}'

            $ {{command}} {1} --editor='user:test-user@gmail.com'

          See https://cloud.google.com/iam/docs/managing-policies for details
          of policy role and member types.
          """.format(collection, example_id)
  }
