"""Generated client library for iam version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from googlecloudsdk.third_party.apitools.base.py import base_api
from googlecloudsdk.third_party.apis.iam.v1 import iam_v1_messages as messages


class IamV1(base_api.BaseApiClient):
  """Generated client library for service iam version v1."""

  MESSAGES_MODULE = messages

  _PACKAGE = u'iam'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'IamV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new iam handle."""
    url = url or u'https://iam.googleapis.com/'
    super(IamV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.iamPolicies = self.IamPoliciesService(self)
    self.projects_serviceAccounts_keys = self.ProjectsServiceAccountsKeysService(self)
    self.projects_serviceAccounts = self.ProjectsServiceAccountsService(self)
    self.projects = self.ProjectsService(self)
    self.roles = self.RolesService(self)

  class IamPoliciesService(base_api.BaseApiService):
    """Service class for the iamPolicies resource."""

    _NAME = u'iamPolicies'

    def __init__(self, client):
      super(IamV1.IamPoliciesService, self).__init__(client)
      self._method_configs = {
          'GetPolicyDetails': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'iam.iamPolicies.getPolicyDetails',
              ordered_params=[],
              path_params=[],
              query_params=[],
              relative_path=u'v1/iamPolicies:getPolicyDetails',
              request_field='<request>',
              request_type_name=u'GetPolicyDetailsRequest',
              response_type_name=u'GetPolicyDetailsResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def GetPolicyDetails(self, request, global_params=None):
      """Returns the current policy and the policies on the inherited resources.
the user has access to.

      Args:
        request: (GetPolicyDetailsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetPolicyDetailsResponse) The response message.
      """
      config = self.GetMethodConfig('GetPolicyDetails')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsServiceAccountsKeysService(base_api.BaseApiService):
    """Service class for the projects_serviceAccounts_keys resource."""

    _NAME = u'projects_serviceAccounts_keys'

    def __init__(self, client):
      super(IamV1.ProjectsServiceAccountsKeysService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'iam.projects.serviceAccounts.keys.create',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}/keys',
              request_field=u'createServiceAccountKeyRequest',
              request_type_name=u'IamProjectsServiceAccountsKeysCreateRequest',
              response_type_name=u'ServiceAccountKey',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'iam.projects.serviceAccounts.keys.delete',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}',
              request_field='',
              request_type_name=u'IamProjectsServiceAccountsKeysDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'iam.projects.serviceAccounts.keys.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}',
              request_field='',
              request_type_name=u'IamProjectsServiceAccountsKeysGetRequest',
              response_type_name=u'ServiceAccountKey',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'iam.projects.serviceAccounts.keys.list',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'keyTypes'],
              relative_path=u'v1/{+name}/keys',
              request_field='',
              request_type_name=u'IamProjectsServiceAccountsKeysListRequest',
              response_type_name=u'ListServiceAccountKeysResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a service account key and returns it.

      Args:
        request: (IamProjectsServiceAccountsKeysCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServiceAccountKey) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes a service account key.

      Args:
        request: (IamProjectsServiceAccountsKeysDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets the ServiceAccountKey.
by key id.

      Args:
        request: (IamProjectsServiceAccountsKeysGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServiceAccountKey) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists service account keys.

      Args:
        request: (IamProjectsServiceAccountsKeysListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListServiceAccountKeysResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsServiceAccountsService(base_api.BaseApiService):
    """Service class for the projects_serviceAccounts resource."""

    _NAME = u'projects_serviceAccounts'

    def __init__(self, client):
      super(IamV1.ProjectsServiceAccountsService, self).__init__(client)
      self._method_configs = {
          'Create': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'iam.projects.serviceAccounts.create',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}/serviceAccounts',
              request_field=u'createServiceAccountRequest',
              request_type_name=u'IamProjectsServiceAccountsCreateRequest',
              response_type_name=u'ServiceAccount',
              supports_download=False,
          ),
          'Delete': base_api.ApiMethodInfo(
              http_method=u'DELETE',
              method_id=u'iam.projects.serviceAccounts.delete',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}',
              request_field='',
              request_type_name=u'IamProjectsServiceAccountsDeleteRequest',
              response_type_name=u'Empty',
              supports_download=False,
          ),
          'Get': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'iam.projects.serviceAccounts.get',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}',
              request_field='',
              request_type_name=u'IamProjectsServiceAccountsGetRequest',
              response_type_name=u'ServiceAccount',
              supports_download=False,
          ),
          'GetIamPolicy': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'iam.projects.serviceAccounts.getIamPolicy',
              ordered_params=[u'resource'],
              path_params=[u'resource'],
              query_params=[],
              relative_path=u'v1/{+resource}:getIamPolicy',
              request_field='',
              request_type_name=u'IamProjectsServiceAccountsGetIamPolicyRequest',
              response_type_name=u'Policy',
              supports_download=False,
          ),
          'List': base_api.ApiMethodInfo(
              http_method=u'GET',
              method_id=u'iam.projects.serviceAccounts.list',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[u'pageSize', u'pageToken', u'removeDeletedServiceAccounts'],
              relative_path=u'v1/{+name}/serviceAccounts',
              request_field='',
              request_type_name=u'IamProjectsServiceAccountsListRequest',
              response_type_name=u'ListServiceAccountsResponse',
              supports_download=False,
          ),
          'SetIamPolicy': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'iam.projects.serviceAccounts.setIamPolicy',
              ordered_params=[u'resource'],
              path_params=[u'resource'],
              query_params=[],
              relative_path=u'v1/{+resource}:setIamPolicy',
              request_field=u'setIamPolicyRequest',
              request_type_name=u'IamProjectsServiceAccountsSetIamPolicyRequest',
              response_type_name=u'Policy',
              supports_download=False,
          ),
          'SignBlob': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'iam.projects.serviceAccounts.signBlob',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}:signBlob',
              request_field=u'signBlobRequest',
              request_type_name=u'IamProjectsServiceAccountsSignBlobRequest',
              response_type_name=u'SignBlobResponse',
              supports_download=False,
          ),
          'TestIamPermissions': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'iam.projects.serviceAccounts.testIamPermissions',
              ordered_params=[u'resource'],
              path_params=[u'resource'],
              query_params=[],
              relative_path=u'v1/{+resource}:testIamPermissions',
              request_field=u'testIamPermissionsRequest',
              request_type_name=u'IamProjectsServiceAccountsTestIamPermissionsRequest',
              response_type_name=u'TestIamPermissionsResponse',
              supports_download=False,
          ),
          'Update': base_api.ApiMethodInfo(
              http_method=u'PUT',
              method_id=u'iam.projects.serviceAccounts.update',
              ordered_params=[u'name'],
              path_params=[u'name'],
              query_params=[],
              relative_path=u'v1/{+name}',
              request_field='<request>',
              request_type_name=u'ServiceAccount',
              response_type_name=u'ServiceAccount',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a service account and returns it.

      Args:
        request: (IamProjectsServiceAccountsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServiceAccount) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Delete(self, request, global_params=None):
      """Deletes a service acount.

      Args:
        request: (IamProjectsServiceAccountsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Get(self, request, global_params=None):
      """Gets a ServiceAccount.

      Args:
        request: (IamProjectsServiceAccountsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServiceAccount) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    def GetIamPolicy(self, request, global_params=None):
      """Returns the IAM access control policy for specified IAM resource.

      Args:
        request: (IamProjectsServiceAccountsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    def List(self, request, global_params=None):
      """Lists service accounts for a project.

      Args:
        request: (IamProjectsServiceAccountsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListServiceAccountsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    def SetIamPolicy(self, request, global_params=None):
      """Sets the IAM access control policy for the specified IAM resource.

      Args:
        request: (IamProjectsServiceAccountsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    def SignBlob(self, request, global_params=None):
      """Signs a blob using a service account.

      Args:
        request: (IamProjectsServiceAccountsSignBlobRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SignBlobResponse) The response message.
      """
      config = self.GetMethodConfig('SignBlob')
      return self._RunMethod(
          config, request, global_params=global_params)

    def TestIamPermissions(self, request, global_params=None):
      """Tests the specified permissions against the IAM access control policy.
for the specified IAM resource.

      Args:
        request: (IamProjectsServiceAccountsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    def Update(self, request, global_params=None):
      """Updates a service account.

Currently, only the following fields are updatable:
'display_name' .
The 'etag' is mandatory.

      Args:
        request: (ServiceAccount) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServiceAccount) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(IamV1.ProjectsService, self).__init__(client)
      self._method_configs = {
          }

      self._upload_configs = {
          }

  class RolesService(base_api.BaseApiService):
    """Service class for the roles resource."""

    _NAME = u'roles'

    def __init__(self, client):
      super(IamV1.RolesService, self).__init__(client)
      self._method_configs = {
          'QueryGrantableRoles': base_api.ApiMethodInfo(
              http_method=u'POST',
              method_id=u'iam.roles.queryGrantableRoles',
              ordered_params=[],
              path_params=[],
              query_params=[],
              relative_path=u'v1/roles:queryGrantableRoles',
              request_field='<request>',
              request_type_name=u'QueryGrantableRolesRequest',
              response_type_name=u'QueryGrantableRolesResponse',
              supports_download=False,
          ),
          }

      self._upload_configs = {
          }

    def QueryGrantableRoles(self, request, global_params=None):
      """Queries roles that can be granted on a particular resource.

      Args:
        request: (QueryGrantableRolesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (QueryGrantableRolesResponse) The response message.
      """
      config = self.GetMethodConfig('QueryGrantableRoles')
      return self._RunMethod(
          config, request, global_params=global_params)
