"""Generated client library for iam version v2alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.iam.v2alpha1 import iam_v2alpha1_messages as messages


class IamV2alpha1(base_api.BaseApiClient):
  """Generated client library for service iam version v2alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://iam.googleapis.com/'
  MTLS_BASE_URL = 'https://iam.mtls.googleapis.com/'

  _PACKAGE = 'iam'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v2alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'IamV2alpha1'
  _URL_VERSION = 'v2alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new iam handle."""
    url = url or self.BASE_URL
    super(IamV2alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.policies = self.PoliciesService(self)

  class PoliciesService(base_api.BaseApiService):
    """Service class for the policies resource."""

    _NAME = 'policies'

    def __init__(self, client):
      super(IamV2alpha1.PoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def CreatePolicy(self, request, global_params=None):
      r"""Creates a policy.

All the policies attached to a specific resource must have unique IDs.

      Args:
        request: (IamPoliciesCreatePolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV2alpha1Policy) The response message.
      """
      config = self.GetMethodConfig('CreatePolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    CreatePolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/policies/{policiesId}/{policiesId1}',
        http_method='POST',
        method_id='iam.policies.createPolicy',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['policyId'],
        relative_path='v2alpha1/{+parent}',
        request_field='googleIamV2alpha1Policy',
        request_type_name='IamPoliciesCreatePolicyRequest',
        response_type_name='GoogleIamV2alpha1Policy',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a policy.

      Args:
        request: (IamPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleProtobufEmpty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/policies/{policiesId}/{policiesId1}/{policiesId2}',
        http_method='DELETE',
        method_id='iam.policies.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['etag'],
        relative_path='v2alpha1/{+name}',
        request_field='',
        request_type_name='IamPoliciesDeleteRequest',
        response_type_name='GoogleProtobufEmpty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets a policy.

      Args:
        request: (IamPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV2alpha1Policy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/policies/{policiesId}/{policiesId1}/{policiesId2}',
        http_method='GET',
        method_id='iam.policies.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}',
        request_field='',
        request_type_name='IamPoliciesGetRequest',
        response_type_name='GoogleIamV2alpha1Policy',
        supports_download=False,
    )

    def ListPolicies(self, request, global_params=None):
      r"""Retrieves all of the policies attached to the specified resource,.
of the given kind.

Only policy metadata is listed; specifically `policy.rules` is omitted.

      Args:
        request: (IamPoliciesListPoliciesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV2alpha1ListPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('ListPolicies')
      return self._RunMethod(
          config, request, global_params=global_params)

    ListPolicies.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/policies/{policiesId}/{policiesId1}',
        http_method='GET',
        method_id='iam.policies.listPolicies',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v2alpha1/{+parent}',
        request_field='',
        request_type_name='IamPoliciesListPoliciesRequest',
        response_type_name='GoogleIamV2alpha1ListPoliciesResponse',
        supports_download=False,
    )

    def ReplacePolicy(self, request, global_params=None):
      r"""Replaces the specified existing policy.

Only `Policy.rules` and `Policy.description` may be updated.

Need to provide etag to enforce update from last read for optimistic
concurrency control.

      Args:
        request: (GoogleIamV2alpha1Policy) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleIamV2alpha1Policy) The response message.
      """
      config = self.GetMethodConfig('ReplacePolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReplacePolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v2alpha1/policies/{policiesId}/{policiesId1}/{policiesId2}',
        http_method='PUT',
        method_id='iam.policies.replacePolicy',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v2alpha1/{+name}',
        request_field='<request>',
        request_type_name='GoogleIamV2alpha1Policy',
        response_type_name='GoogleIamV2alpha1Policy',
        supports_download=False,
    )
