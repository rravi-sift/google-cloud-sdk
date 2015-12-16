"""Generated client library for cloudfunctions version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from googlecloudsdk.third_party.apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudfunctions.v1beta1 import cloudfunctions_v1beta1_messages as messages


class CloudfunctionsV1beta1(base_api.BaseApiClient):
  """Generated client library for service cloudfunctions version v1beta1."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'cloudfunctions'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/pubsub']
  _VERSION = u'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudfunctionsV1beta1'
  _URL_VERSION = u'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new cloudfunctions handle."""
    url = url or u'https://cloudfunctions.googleapis.com/'
    super(CloudfunctionsV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.operations = self.OperationsService(self)
    self.projects_regions_functions = self.ProjectsRegionsFunctionsService(self)
    self.projects_regions = self.ProjectsRegionsService(self)
    self.projects = self.ProjectsService(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = u'operations'

    def __init__(self, client):
      super(CloudfunctionsV1beta1.OperationsService, self).__init__(client)
      self._method_configs = {
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'cloudfunctions.operations.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta1/{+name}',
              request_field='',
              request_type_name=u'CloudfunctionsOperationsGetRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      """Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (CloudfunctionsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsRegionsFunctionsService(base_api.BaseApiService):
    """Service class for the projects_regions_functions resource."""

    _NAME = u'projects_regions_functions'

    def __init__(self, client):
      super(CloudfunctionsV1beta1.ProjectsRegionsFunctionsService, self).__init__(client)
      self._method_configs = {
          'Call': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'cloudfunctions.projects.regions.functions.call',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'data'],
              relative_path=u'v1beta1/{+name}:call',
              request_field='',
              request_type_name=u'CloudfunctionsProjectsRegionsFunctionsCallRequest',
              response_type_name=u'CallFunctionResponse',
              supports_download=False,
          ),
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'cloudfunctions.projects.regions.functions.create',
              ordered_params=[u'location'],
              path_params=[u'location'],
              query_params=[],
              relative_path=u'v1beta1/{+location}/functions',
              request_field=u'hostedFunction',
              request_type_name=u'CloudfunctionsProjectsRegionsFunctionsCreateRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'cloudfunctions.projects.regions.functions.delete',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta1/{+name}',
              request_field='',
              request_type_name=u'CloudfunctionsProjectsRegionsFunctionsDeleteRequest',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'cloudfunctions.projects.regions.functions.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta1/{+name}',
              request_field='',
              request_type_name=u'CloudfunctionsProjectsRegionsFunctionsGetRequest',
              response_type_name=u'HostedFunction',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'cloudfunctions.projects.regions.functions.list',
              ordered_params=[u'location'],
              path_params=[u'location'],
              query_params=[u'pageSize', u'pageToken'],
              relative_path=u'v1beta1/{+location}/functions',
              request_field='',
              request_type_name=u'CloudfunctionsProjectsRegionsFunctionsListRequest',
              response_type_name=u'ListFunctionsResponse',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'cloudfunctions.projects.regions.functions.update',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1beta1/{+name}',
              request_field='<request>',
              request_type_name=u'HostedFunction',
              response_type_name=u'Operation',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Call(self, request, global_params=None):
      """Invokes synchronously deployed function. To be used for testing, very.
limited traffic allowed.

      Args:
        request: (CloudfunctionsProjectsRegionsFunctionsCallRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CallFunctionResponse) The response message.
      """
      config = self.GetMethodConfig('Call')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Create(self, request, global_params=None):
      """Creates a new function. If a function with the given name already exists in.
the specified project, it will return ALREADY_EXISTS error.

      Args:
        request: (CloudfunctionsProjectsRegionsFunctionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes a function with the given name from the specified project. If the.
given function is used by some trigger, the trigger will be updated to
remove this function.

      Args:
        request: (CloudfunctionsProjectsRegionsFunctionsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Returns a function with the given name from the requested project.

      Args:
        request: (CloudfunctionsProjectsRegionsFunctionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (HostedFunction) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Returns a list of all functions that belong to the requested project.

      Args:
        request: (CloudfunctionsProjectsRegionsFunctionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListFunctionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Updates existing function.

      Args:
        request: (HostedFunction) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsRegionsService(base_api.BaseApiService):
    """Service class for the projects_regions resource."""

    _NAME = u'projects_regions'

    def __init__(self, client):
      super(CloudfunctionsV1beta1.ProjectsRegionsService, self).__init__(client)
      self._method_configs = {
          }

      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(CloudfunctionsV1beta1.ProjectsService, self).__init__(client)
      self._method_configs = {
          }

      self._upload_configs = {
          }
