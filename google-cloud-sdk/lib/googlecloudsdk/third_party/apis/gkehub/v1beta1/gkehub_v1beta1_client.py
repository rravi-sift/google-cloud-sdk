"""Generated client library for gkehub version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.gkehub.v1beta1 import gkehub_v1beta1_messages as messages


class GkehubV1beta1(base_api.BaseApiClient):
  """Generated client library for service gkehub version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://gkehub.googleapis.com/'
  MTLS_BASE_URL = 'https://gkehub.mtls.googleapis.com/'

  _PACKAGE = 'gkehub'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'GkehubV1beta1'
  _URL_VERSION = 'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new gkehub handle."""
    url = url or self.BASE_URL
    super(GkehubV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_memberships = self.ProjectsLocationsMembershipsService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsMembershipsService(base_api.BaseApiService):
    """Service class for the projects_locations_memberships resource."""

    _NAME = 'projects_locations_memberships'

    def __init__(self, client):
      super(GkehubV1beta1.ProjectsLocationsMembershipsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Adds a new Membership.

      Args:
        request: (GkehubProjectsLocationsMembershipsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/memberships',
        http_method='POST',
        method_id='gkehub.projects.locations.memberships.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['membershipId'],
        relative_path='v1beta1/{+parent}/memberships',
        request_field='membership',
        request_type_name='GkehubProjectsLocationsMembershipsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Removes a single Membership.

      Args:
        request: (GkehubProjectsLocationsMembershipsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/memberships/{membershipsId}',
        http_method='DELETE',
        method_id='gkehub.projects.locations.memberships.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='GkehubProjectsLocationsMembershipsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def GenerateConnectManifest(self, request, global_params=None):
      r"""Generate the manifest for deployment of GKE connect agent.

      Args:
        request: (GkehubProjectsLocationsMembershipsGenerateConnectManifestRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GenerateConnectManifestResponse) The response message.
      """
      config = self.GetMethodConfig('GenerateConnectManifest')
      return self._RunMethod(
          config, request, global_params=global_params)

    GenerateConnectManifest.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/memberships/{membershipsId}:generateConnectManifest',
        http_method='GET',
        method_id='gkehub.projects.locations.memberships.generateConnectManifest',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['connectAgent_name', 'connectAgent_namespace', 'connectAgent_proxy', 'imagePullSecretContent', 'isUpgrade', 'registry', 'version'],
        relative_path='v1beta1/{+name}:generateConnectManifest',
        request_field='',
        request_type_name='GkehubProjectsLocationsMembershipsGenerateConnectManifestRequest',
        response_type_name='GenerateConnectManifestResponse',
        supports_download=False,
    )

    def GenerateExclusivityManifest(self, request, global_params=None):
      r"""GenerateExclusivityManifest generates the manifests to update the.
exclusivity artifacts in the cluster if needed.
Exclusivity artifacts include the membership customer resource definition
(CRD) and the singleton membership custom resource (CR).
Combined with ValidateExclusivity, exclusivity
artifacts guarantee that a Kubernetes cluster is only registered to
a single GKE Hub.
The membership CRD is versioned, and may require conversion when the GKE
Hub API server begins serving a newer version of the CRD and
corresponding CR. The response will be the converted CRD and CR if there
are any differences between the versions.

      Args:
        request: (GkehubProjectsLocationsMembershipsGenerateExclusivityManifestRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GenerateExclusivityManifestResponse) The response message.
      """
      config = self.GetMethodConfig('GenerateExclusivityManifest')
      return self._RunMethod(
          config, request, global_params=global_params)

    GenerateExclusivityManifest.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/memberships/{membershipsId}:generateExclusivityManifest',
        http_method='GET',
        method_id='gkehub.projects.locations.memberships.generateExclusivityManifest',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['crManifest', 'crdManifest'],
        relative_path='v1beta1/{+name}:generateExclusivityManifest',
        request_field='',
        request_type_name='GkehubProjectsLocationsMembershipsGenerateExclusivityManifestRequest',
        response_type_name='GenerateExclusivityManifestResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Membership.

      Args:
        request: (GkehubProjectsLocationsMembershipsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Membership) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/memberships/{membershipsId}',
        http_method='GET',
        method_id='gkehub.projects.locations.memberships.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='GkehubProjectsLocationsMembershipsGetRequest',
        response_type_name='Membership',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (GkehubProjectsLocationsMembershipsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/memberships/{membershipsId}:getIamPolicy',
        http_method='GET',
        method_id='gkehub.projects.locations.memberships.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1beta1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='GkehubProjectsLocationsMembershipsGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Memberships in a given project and location.

      Args:
        request: (GkehubProjectsLocationsMembershipsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListMembershipsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/memberships',
        http_method='GET',
        method_id='gkehub.projects.locations.memberships.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/memberships',
        request_field='',
        request_type_name='GkehubProjectsLocationsMembershipsListRequest',
        response_type_name='ListMembershipsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates an existing Membership.

      Args:
        request: (GkehubProjectsLocationsMembershipsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/memberships/{membershipsId}',
        http_method='PATCH',
        method_id='gkehub.projects.locations.memberships.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1beta1/{+name}',
        request_field='membership',
        request_type_name='GkehubProjectsLocationsMembershipsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any.
existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

      Args:
        request: (GkehubProjectsLocationsMembershipsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/memberships/{membershipsId}:setIamPolicy',
        http_method='POST',
        method_id='gkehub.projects.locations.memberships.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='GkehubProjectsLocationsMembershipsSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (GkehubProjectsLocationsMembershipsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/memberships/{membershipsId}:testIamPermissions',
        http_method='POST',
        method_id='gkehub.projects.locations.memberships.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='GkehubProjectsLocationsMembershipsTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

    def ValidateExclusivity(self, request, global_params=None):
      r"""ValidateExclusivity validates the state of exclusivity in the cluster.
The validation does not depend on an existing Hub membership resource.

      Args:
        request: (GkehubProjectsLocationsMembershipsValidateExclusivityRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ValidateExclusivityResponse) The response message.
      """
      config = self.GetMethodConfig('ValidateExclusivity')
      return self._RunMethod(
          config, request, global_params=global_params)

    ValidateExclusivity.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/memberships:validateExclusivity',
        http_method='GET',
        method_id='gkehub.projects.locations.memberships.validateExclusivity',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['crManifest', 'intendedMembership'],
        relative_path='v1beta1/{+parent}/memberships:validateExclusivity',
        request_field='',
        request_type_name='GkehubProjectsLocationsMembershipsValidateExclusivityRequest',
        response_type_name='ValidateExclusivityResponse',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(GkehubV1beta1.ProjectsLocationsOperationsService, self).__init__(client)
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
        request: (GkehubProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='gkehub.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='GkehubProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (GkehubProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='gkehub.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='GkehubProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (GkehubProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='gkehub.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='GkehubProjectsLocationsOperationsGetRequest',
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
        request: (GkehubProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='gkehub.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+name}/operations',
        request_field='',
        request_type_name='GkehubProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(GkehubV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (GkehubProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='gkehub.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='GkehubProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (GkehubProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='gkehub.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'includeUnrevealedLocations', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+name}/locations',
        request_field='',
        request_type_name='GkehubProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(GkehubV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
