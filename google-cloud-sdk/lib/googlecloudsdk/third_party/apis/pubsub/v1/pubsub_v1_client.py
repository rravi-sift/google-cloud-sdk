"""Generated client library for pubsub version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from googlecloudsdk.third_party.apitools.base.py import base_api
from googlecloudsdk.third_party.apis.pubsub.v1 import pubsub_v1_messages as messages


class PubsubV1(base_api.BaseApiClient):
  """Generated client library for service pubsub version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://pubsub.googleapis.com/'

  _PACKAGE = u'pubsub'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/pubsub']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'PubsubV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new pubsub handle."""
    url = url or self.BASE_URL
    super(PubsubV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_subscriptions = self.ProjectsSubscriptionsService(self)
    self.projects_topics_subscriptions = self.ProjectsTopicsSubscriptionsService(self)
    self.projects_topics = self.ProjectsTopicsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsSubscriptionsService(base_api.BaseApiService):
    """Service class for the projects_subscriptions resource."""

    _NAME = u'projects_subscriptions'

    def __init__(self, client):
      super(PubsubV1.ProjectsSubscriptionsService, self).__init__(client)
      self._method_configs = {
          'Acknowledge': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/subscriptions/{subscriptionsId}:acknowledge',
              http_method=u'POST',
              method_id=u'pubsub.projects.subscriptions.acknowledge',
              ordered_params=[u'subscription'],
              path_params=[u'subscription'],
              query_params=[],
              relative_path=u'v1/{+subscription}:acknowledge',
              request_field=u'acknowledgeRequest',
              request_type_name=u'PubsubProjectsSubscriptionsAcknowledgeRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Create': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/subscriptions/{subscriptionsId}',
              http_method=u'PUT',
              method_id=u'pubsub.projects.subscriptions.create',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}',
              request_field='<request>',
              request_type_name=u'Subscription',
              response_type_name=u'Subscription',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/subscriptions/{subscriptionsId}',
              http_method=u'DELETE',
              method_id=u'pubsub.projects.subscriptions.delete',
              ordered_params=[u'subscription'],
              path_params=[u'subscription'],
              query_params=[],
              relative_path=u'v1/{+subscription}',
              request_field='',
              request_type_name=u'PubsubProjectsSubscriptionsDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/subscriptions/{subscriptionsId}',
              http_method=u'GET',
              method_id=u'pubsub.projects.subscriptions.get',
              ordered_params=[u'subscription'],
              path_params=[u'subscription'],
              query_params=[],
              relative_path=u'v1/{+subscription}',
              request_field='',
              request_type_name=u'PubsubProjectsSubscriptionsGetRequest',
              response_type_name=u'Subscription',
              supports_download=False,
          ),
          'GetIamPolicy': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/subscriptions/{subscriptionsId}:getIamPolicy',
              http_method=u'GET',
              method_id=u'pubsub.projects.subscriptions.getIamPolicy',
              ordered_params=[u'resource'],
              path_params=[u'resource'],
              query_params=[],
              relative_path=u'v1/{+resource}:getIamPolicy',
              request_field='',
              request_type_name=u'PubsubProjectsSubscriptionsGetIamPolicyRequest',
              response_type_name=u'Policy',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/subscriptions',
              http_method=u'GET',
              method_id=u'pubsub.projects.subscriptions.list',
              ordered_params=[u'project'],
              path_params=[u'project'],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v1/{+project}/subscriptions',
              request_field='',
              request_type_name=u'PubsubProjectsSubscriptionsListRequest',
              response_type_name=u'ListSubscriptionsResponse',
              supports_download=False,
          ),
          'ModifyAckDeadline': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/subscriptions/{subscriptionsId}:modifyAckDeadline',
              http_method=u'POST',
              method_id=u'pubsub.projects.subscriptions.modifyAckDeadline',
              ordered_params=[u'subscription'],
              path_params=[u'subscription'],
              query_params=[],
              relative_path=u'v1/{+subscription}:modifyAckDeadline',
              request_field=u'modifyAckDeadlineRequest',
              request_type_name=u'PubsubProjectsSubscriptionsModifyAckDeadlineRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'ModifyPushConfig': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/subscriptions/{subscriptionsId}:modifyPushConfig',
              http_method=u'POST',
              method_id=u'pubsub.projects.subscriptions.modifyPushConfig',
              ordered_params=[u'subscription'],
              path_params=[u'subscription'],
              query_params=[],
              relative_path=u'v1/{+subscription}:modifyPushConfig',
              request_field=u'modifyPushConfigRequest',
              request_type_name=u'PubsubProjectsSubscriptionsModifyPushConfigRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Pull': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/subscriptions/{subscriptionsId}:pull',
              http_method=u'POST',
              method_id=u'pubsub.projects.subscriptions.pull',
              ordered_params=[u'subscription'],
              path_params=[u'subscription'],
              query_params=[],
              relative_path=u'v1/{+subscription}:pull',
              request_field=u'pullRequest',
              request_type_name=u'PubsubProjectsSubscriptionsPullRequest',
              response_type_name=u'PullResponse',
              supports_download=False,
          ),
          'SetIamPolicy': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/subscriptions/{subscriptionsId}:setIamPolicy',
              http_method=u'POST',
              method_id=u'pubsub.projects.subscriptions.setIamPolicy',
              ordered_params=[u'resource'],
              path_params=[u'resource'],
              query_params=[],
              relative_path=u'v1/{+resource}:setIamPolicy',
              request_field=u'setIamPolicyRequest',
              request_type_name=u'PubsubProjectsSubscriptionsSetIamPolicyRequest',
              response_type_name=u'Policy',
              supports_download=False,
          ),
          'TestIamPermissions': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/subscriptions/{subscriptionsId}:testIamPermissions',
              http_method=u'POST',
              method_id=u'pubsub.projects.subscriptions.testIamPermissions',
              ordered_params=[u'resource'],
              path_params=[u'resource'],
              query_params=[],
              relative_path=u'v1/{+resource}:testIamPermissions',
              request_field=u'testIamPermissionsRequest',
              request_type_name=u'PubsubProjectsSubscriptionsTestIamPermissionsRequest',
              response_type_name=u'TestIamPermissionsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Acknowledge(self, request, global_params=None):
      """Acknowledges the messages associated with the `ack_ids` in the.
`AcknowledgeRequest`. The Pub/Sub system can remove the relevant messages
from the subscription.

Acknowledging a message whose ack deadline has expired may succeed,
but such a message may be redelivered later. Acknowledging a message more
than once will not result in an error.

      Args:
        request: (PubsubProjectsSubscriptionsAcknowledgeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Acknowledge')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Create(self, request, global_params=None):
      """Creates a subscription to a given topic.
If the subscription already exists, returns `ALREADY_EXISTS`.
If the corresponding topic doesn't exist, returns `NOT_FOUND`.

If the name is not provided in the request, the server will assign a random
name for this subscription on the same project as the topic.

      Args:
        request: (Subscription) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Subscription) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes an existing subscription. All pending messages in the subscription.
are immediately dropped. Calls to `Pull` after deletion will return
`NOT_FOUND`. After a subscription is deleted, a new one may be created with
the same name, but the new one has no association with the old
subscription, or its topic unless the same topic is specified.

      Args:
        request: (PubsubProjectsSubscriptionsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets the configuration details of a subscription.

      Args:
        request: (PubsubProjectsSubscriptionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Subscription) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def GetIamPolicy(self, request, global_params=None):
      """Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (PubsubProjectsSubscriptionsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists matching subscriptions.

      Args:
        request: (PubsubProjectsSubscriptionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListSubscriptionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def ModifyAckDeadline(self, request, global_params=None):
      """Modifies the ack deadline for a specific message. This method is useful.
to indicate that more time is needed to process a message by the
subscriber, or to make the message available for redelivery if the
processing was interrupted.

      Args:
        request: (PubsubProjectsSubscriptionsModifyAckDeadlineRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('ModifyAckDeadline')
      return self._RunMethod(
          config, request, global_params=global_params)

    def ModifyPushConfig(self, request, global_params=None):
      """Modifies the `PushConfig` for a specified subscription.

This may be used to change a push subscription to a pull one (signified by
an empty `PushConfig`) or vice versa, or change the endpoint URL and other
attributes of a push subscription. Messages will accumulate for delivery
continuously through the call regardless of changes to the `PushConfig`.

      Args:
        request: (PubsubProjectsSubscriptionsModifyPushConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('ModifyPushConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Pull(self, request, global_params=None):
      """Pulls messages from the server. Returns an empty list if there are no.
messages available in the backlog. The server may return `UNAVAILABLE` if
there are too many concurrent pull requests pending for the given
subscription.

      Args:
        request: (PubsubProjectsSubscriptionsPullRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PullResponse) The response message.
      """
      config = self.GetMethodConfig('Pull')
      return self._RunMethod(
          config, request, global_params=global_params)

    def SetIamPolicy(self, request, global_params=None):
      """Sets the access control policy on the specified resource. Replaces any.
existing policy.

      Args:
        request: (PubsubProjectsSubscriptionsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    def TestIamPermissions(self, request, global_params=None):
      """Returns permissions that a caller has on the specified resource.

      Args:
        request: (PubsubProjectsSubscriptionsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsTopicsSubscriptionsService(base_api.BaseApiService):
    """Service class for the projects_topics_subscriptions resource."""

    _NAME = u'projects_topics_subscriptions'

    def __init__(self, client):
      super(PubsubV1.ProjectsTopicsSubscriptionsService, self).__init__(client)
      self._method_configs = {
          'List': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/topics/{topicsId}/subscriptions',
              http_method=u'GET',
              method_id=u'pubsub.projects.topics.subscriptions.list',
              ordered_params=[u'topic'],
              path_params=[u'topic'],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v1/{+topic}/subscriptions',
              request_field='',
              request_type_name=u'PubsubProjectsTopicsSubscriptionsListRequest',
              response_type_name=u'ListTopicSubscriptionsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists the name of the subscriptions for this topic.

      Args:
        request: (PubsubProjectsTopicsSubscriptionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTopicSubscriptionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsTopicsService(base_api.BaseApiService):
    """Service class for the projects_topics resource."""

    _NAME = u'projects_topics'

    def __init__(self, client):
      super(PubsubV1.ProjectsTopicsService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/topics/{topicsId}',
              http_method=u'PUT',
              method_id=u'pubsub.projects.topics.create',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}',
              request_field='<request>',
              request_type_name=u'Topic',
              response_type_name=u'Topic',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/topics/{topicsId}',
              http_method=u'DELETE',
              method_id=u'pubsub.projects.topics.delete',
              ordered_params=[u'topic'],
              path_params=[u'topic'],
              query_params=[],
              relative_path=u'v1/{+topic}',
              request_field='',
              request_type_name=u'PubsubProjectsTopicsDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/topics/{topicsId}',
              http_method=u'GET',
              method_id=u'pubsub.projects.topics.get',
              ordered_params=[u'topic'],
              path_params=[u'topic'],
              query_params=[],
              relative_path=u'v1/{+topic}',
              request_field='',
              request_type_name=u'PubsubProjectsTopicsGetRequest',
              response_type_name=u'Topic',
              supports_download=False,
          ),
          'GetIamPolicy': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/topics/{topicsId}:getIamPolicy',
              http_method=u'GET',
              method_id=u'pubsub.projects.topics.getIamPolicy',
              ordered_params=[u'resource'],
              path_params=[u'resource'],
              query_params=[],
              relative_path=u'v1/{+resource}:getIamPolicy',
              request_field='',
              request_type_name=u'PubsubProjectsTopicsGetIamPolicyRequest',
              response_type_name=u'Policy',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/topics',
              http_method=u'GET',
              method_id=u'pubsub.projects.topics.list',
              ordered_params=[u'project'],
              path_params=[u'project'],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v1/{+project}/topics',
              request_field='',
              request_type_name=u'PubsubProjectsTopicsListRequest',
              response_type_name=u'ListTopicsResponse',
              supports_download=False,
          ),
          'Publish': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/topics/{topicsId}:publish',
              http_method=u'POST',
              method_id=u'pubsub.projects.topics.publish',
              ordered_params=[u'topic'],
              path_params=[u'topic'],
              query_params=[],
              relative_path=u'v1/{+topic}:publish',
              request_field=u'publishRequest',
              request_type_name=u'PubsubProjectsTopicsPublishRequest',
              response_type_name=u'PublishResponse',
              supports_download=False,
          ),
          'SetIamPolicy': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/topics/{topicsId}:setIamPolicy',
              http_method=u'POST',
              method_id=u'pubsub.projects.topics.setIamPolicy',
              ordered_params=[u'resource'],
              path_params=[u'resource'],
              query_params=[],
              relative_path=u'v1/{+resource}:setIamPolicy',
              request_field=u'setIamPolicyRequest',
              request_type_name=u'PubsubProjectsTopicsSetIamPolicyRequest',
              response_type_name=u'Policy',
              supports_download=False,
          ),
          'TestIamPermissions': base_api.ApiMethodInfo(
              flat_path=u'v1/projects/{projectsId}/topics/{topicsId}:testIamPermissions',
              http_method=u'POST',
              method_id=u'pubsub.projects.topics.testIamPermissions',
              ordered_params=[u'resource'],
              path_params=[u'resource'],
              query_params=[],
              relative_path=u'v1/{+resource}:testIamPermissions',
              request_field=u'testIamPermissionsRequest',
              request_type_name=u'PubsubProjectsTopicsTestIamPermissionsRequest',
              response_type_name=u'TestIamPermissionsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates the given topic with the given name.

      Args:
        request: (Topic) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Topic) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes the topic with the given name. Returns `NOT_FOUND` if the topic.
does not exist. After a topic is deleted, a new topic may be created with
the same name; this is an entirely new topic with none of the old
configuration or subscriptions. Existing subscriptions to this topic are
not deleted, but their `topic` field is set to `_deleted-topic_`.

      Args:
        request: (PubsubProjectsTopicsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets the configuration of a topic.

      Args:
        request: (PubsubProjectsTopicsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Topic) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def GetIamPolicy(self, request, global_params=None):
      """Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (PubsubProjectsTopicsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists matching topics.

      Args:
        request: (PubsubProjectsTopicsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListTopicsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Publish(self, request, global_params=None):
      """Adds one or more messages to the topic. Returns `NOT_FOUND` if the topic.
does not exist. The message payload must not be empty; it must contain
 either a non-empty data field, or at least one attribute.

      Args:
        request: (PubsubProjectsTopicsPublishRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PublishResponse) The response message.
      """
      config = self.GetMethodConfig('Publish')
      return self._RunMethod(
          config, request, global_params=global_params)

    def SetIamPolicy(self, request, global_params=None):
      """Sets the access control policy on the specified resource. Replaces any.
existing policy.

      Args:
        request: (PubsubProjectsTopicsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    def TestIamPermissions(self, request, global_params=None):
      """Returns permissions that a caller has on the specified resource.

      Args:
        request: (PubsubProjectsTopicsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(PubsubV1.ProjectsService, self).__init__(client)
      self._method_configs = {
          }

      self._upload_configs = {
          }
