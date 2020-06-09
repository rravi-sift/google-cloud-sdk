"""Generated client library for cloudbuild version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudbuild.v1 import cloudbuild_v1_messages as messages


class CloudbuildV1(base_api.BaseApiClient):
  """Generated client library for service cloudbuild version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudbuild.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudbuild.mtls.googleapis.com/'

  _PACKAGE = 'cloudbuild'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudbuildV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudbuild handle."""
    url = url or self.BASE_URL
    super(CloudbuildV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.operations = self.OperationsService(self)
    self.projects_builds = self.ProjectsBuildsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects_triggers = self.ProjectsTriggersService(self)
    self.projects = self.ProjectsService(self)
    self.vbeta1_projects_locations_operations = self.Vbeta1ProjectsLocationsOperationsService(self)
    self.vbeta1_projects_locations = self.Vbeta1ProjectsLocationsService(self)
    self.vbeta1_projects = self.Vbeta1ProjectsService(self)
    self.vbeta1 = self.Vbeta1Service(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = 'operations'

    def __init__(self, client):
      super(CloudbuildV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (CloudbuildOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='cloudbuild.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='CloudbuildOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (CloudbuildOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations/{operationsId}',
        http_method='GET',
        method_id='cloudbuild.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudbuildOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (CloudbuildOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations',
        http_method='GET',
        method_id='cloudbuild.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudbuildOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsBuildsService(base_api.BaseApiService):
    """Service class for the projects_builds resource."""

    _NAME = 'projects_builds'

    def __init__(self, client):
      super(CloudbuildV1.ProjectsBuildsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Cancels a build in progress.

      Args:
        request: (CloudbuildProjectsBuildsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Build) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudbuild.projects.builds.cancel',
        ordered_params=['projectId', 'id'],
        path_params=['id', 'projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/builds/{id}:cancel',
        request_field='cancelBuildRequest',
        request_type_name='CloudbuildProjectsBuildsCancelRequest',
        response_type_name='Build',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Starts a build with the specified configuration.

This method returns a long-running `Operation`, which includes the build
ID. Pass the build ID to `GetBuild` to determine the build status (such as
`SUCCESS` or `FAILURE`).

      Args:
        request: (CloudbuildProjectsBuildsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudbuild.projects.builds.create',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/builds',
        request_field='build',
        request_type_name='CloudbuildProjectsBuildsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Returns information about a previously requested build.

The `Build` that is returned includes its status (such as `SUCCESS`,
`FAILURE`, or `WORKING`), and timing information.

      Args:
        request: (CloudbuildProjectsBuildsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Build) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='cloudbuild.projects.builds.get',
        ordered_params=['projectId', 'id'],
        path_params=['id', 'projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/builds/{id}',
        request_field='',
        request_type_name='CloudbuildProjectsBuildsGetRequest',
        response_type_name='Build',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists previously requested builds.

Previously requested builds may still be in-progress, or may have finished
successfully or unsuccessfully.

      Args:
        request: (CloudbuildProjectsBuildsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListBuildsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='cloudbuild.projects.builds.list',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/projects/{projectId}/builds',
        request_field='',
        request_type_name='CloudbuildProjectsBuildsListRequest',
        response_type_name='ListBuildsResponse',
        supports_download=False,
    )

    def Retry(self, request, global_params=None):
      r"""Creates a new build based on the specified build.

This method creates a new build using the original build request, which may
or may not result in an identical build.

For triggered builds:

* Triggered builds resolve to a precise revision; therefore a retry of a
triggered build will result in a build that uses the same revision.

For non-triggered builds that specify `RepoSource`:

* If the original build built from the tip of a branch, the retried build
will build from the tip of that branch, which may not be the same revision
as the original build.
* If the original build specified a commit sha or revision ID, the retried
build will use the identical source.

For builds that specify `StorageSource`:

* If the original build pulled source from Google Cloud Storage without
specifying the generation of the object, the new build will use the current
object, which may be different from the original build source.
* If the original build pulled source from Cloud Storage and specified the
generation of the object, the new build will attempt to use the same
object, which may or may not be available depending on the bucket's
lifecycle management settings.

      Args:
        request: (CloudbuildProjectsBuildsRetryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Retry')
      return self._RunMethod(
          config, request, global_params=global_params)

    Retry.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudbuild.projects.builds.retry',
        ordered_params=['projectId', 'id'],
        path_params=['id', 'projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/builds/{id}:retry',
        request_field='retryBuildRequest',
        request_type_name='CloudbuildProjectsBuildsRetryRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(CloudbuildV1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (CloudbuildProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='cloudbuild.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='CloudbuildProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (CloudbuildProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='cloudbuild.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='CloudbuildProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (CloudbuildProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='cloudbuild.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}/operations',
        request_field='',
        request_type_name='CloudbuildProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(CloudbuildV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsTriggersService(base_api.BaseApiService):
    """Service class for the projects_triggers resource."""

    _NAME = 'projects_triggers'

    def __init__(self, client):
      super(CloudbuildV1.ProjectsTriggersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new `BuildTrigger`.

This API is experimental.

      Args:
        request: (CloudbuildProjectsTriggersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BuildTrigger) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudbuild.projects.triggers.create',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/triggers',
        request_field='buildTrigger',
        request_type_name='CloudbuildProjectsTriggersCreateRequest',
        response_type_name='BuildTrigger',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a `BuildTrigger` by its project ID and trigger ID.

This API is experimental.

      Args:
        request: (CloudbuildProjectsTriggersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method='DELETE',
        method_id='cloudbuild.projects.triggers.delete',
        ordered_params=['projectId', 'triggerId'],
        path_params=['projectId', 'triggerId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/triggers/{triggerId}',
        request_field='',
        request_type_name='CloudbuildProjectsTriggersDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Returns information about a `BuildTrigger`.

This API is experimental.

      Args:
        request: (CloudbuildProjectsTriggersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BuildTrigger) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='cloudbuild.projects.triggers.get',
        ordered_params=['projectId', 'triggerId'],
        path_params=['projectId', 'triggerId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/triggers/{triggerId}',
        request_field='',
        request_type_name='CloudbuildProjectsTriggersGetRequest',
        response_type_name='BuildTrigger',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists existing `BuildTrigger`s.

This API is experimental.

      Args:
        request: (CloudbuildProjectsTriggersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListBuildTriggersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='cloudbuild.projects.triggers.list',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/projects/{projectId}/triggers',
        request_field='',
        request_type_name='CloudbuildProjectsTriggersListRequest',
        response_type_name='ListBuildTriggersResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a `BuildTrigger` by its project ID and trigger ID.

This API is experimental.

      Args:
        request: (CloudbuildProjectsTriggersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BuildTrigger) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method='PATCH',
        method_id='cloudbuild.projects.triggers.patch',
        ordered_params=['projectId', 'triggerId'],
        path_params=['projectId', 'triggerId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/triggers/{triggerId}',
        request_field='buildTrigger',
        request_type_name='CloudbuildProjectsTriggersPatchRequest',
        response_type_name='BuildTrigger',
        supports_download=False,
    )

    def Run(self, request, global_params=None):
      r"""Runs a `BuildTrigger` at a particular source revision.

      Args:
        request: (CloudbuildProjectsTriggersRunRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Run')
      return self._RunMethod(
          config, request, global_params=global_params)

    Run.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='cloudbuild.projects.triggers.run',
        ordered_params=['projectId', 'triggerId'],
        path_params=['projectId', 'triggerId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/triggers/{triggerId}:run',
        request_field='repoSource',
        request_type_name='CloudbuildProjectsTriggersRunRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(CloudbuildV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

  class Vbeta1ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the vbeta1_projects_locations_operations resource."""

    _NAME = 'vbeta1_projects_locations_operations'

    def __init__(self, client):
      super(CloudbuildV1.Vbeta1ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (CloudbuildVbeta1ProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='vbeta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='cloudbuild.vbeta1.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='vbeta1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='CloudbuildVbeta1ProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

  class Vbeta1ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the vbeta1_projects_locations resource."""

    _NAME = 'vbeta1_projects_locations'

    def __init__(self, client):
      super(CloudbuildV1.Vbeta1ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class Vbeta1ProjectsService(base_api.BaseApiService):
    """Service class for the vbeta1_projects resource."""

    _NAME = 'vbeta1_projects'

    def __init__(self, client):
      super(CloudbuildV1.Vbeta1ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

  class Vbeta1Service(base_api.BaseApiService):
    """Service class for the vbeta1 resource."""

    _NAME = 'vbeta1'

    def __init__(self, client):
      super(CloudbuildV1.Vbeta1Service, self).__init__(client)
      self._upload_configs = {
          }
