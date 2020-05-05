"""Generated message classes for iap version v1.

Controls access to cloud applications running on Google Cloud Platform.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'iap'


class AccessDeniedPageSettings(_messages.Message):
  r"""Custom content configuration for access denied page. IAP allows
  customers to define a custom URI to use as the error page when access is
  denied to users. If IAP prevents access to this page, the default IAP error
  page will be displayed instead.

  Fields:
    accessDeniedPageUri: The URI to be redirected to when access is denied.
  """

  accessDeniedPageUri = _messages.StringField(1)


class AccessSettings(_messages.Message):
  r"""Access related settings for IAP protected apps.

  Fields:
    corsSettings: Configuration to allow cross-origin requests via IAP.
    gcipSettings: GCIP claims and endpoint configurations for 3p identity
      providers.
    oauthSettings: Settings to configure IAP's OAuth behavior.
    policyDelegationSettings: Settings to configure Policy delegation for apps
      hosted in tenant projects. INTERNAL_ONLY.
  """

  corsSettings = _messages.MessageField('CorsSettings', 1)
  gcipSettings = _messages.MessageField('GcipSettings', 2)
  oauthSettings = _messages.MessageField('OAuthSettings', 3)
  policyDelegationSettings = _messages.MessageField('PolicyDelegationSettings', 4)


class ApplicationSettings(_messages.Message):
  r"""Wrapper over application specific settings for IAP.

  Fields:
    accessDeniedPageSettings: Customization for Access Denied page.
    cookieDomain: The Domain value to set for cookies generated by IAP. This
      value is not validated by the API, but will be ignored at runtime if
      invalid.
    csmSettings: Settings to configure IAP's behavior for a CSM mesh.
  """

  accessDeniedPageSettings = _messages.MessageField('AccessDeniedPageSettings', 1)
  cookieDomain = _messages.StringField(2)
  csmSettings = _messages.MessageField('CsmSettings', 3)


class Binding(_messages.Message):
  r"""Associates `members` with a `role`.

  Fields:
    condition: The condition that is associated with this binding.  If the
      condition evaluates to `true`, then this binding applies to the current
      request.  If the condition evaluates to `false`, then this binding does
      not apply to the current request. However, a different role binding
      might grant the same role to one or more of the members in this binding.
      To learn which resources support conditions in their IAM policies, see
      the [IAM documentation](https://cloud.google.com/iam/help/conditions
      /resource-policies).
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following values:  * `allUsers`: A
      special identifier that represents anyone who is    on the internet;
      with or without a Google account.  * `allAuthenticatedUsers`: A special
      identifier that represents anyone    who is authenticated with a Google
      account or a service account.  * `user:{emailid}`: An email address that
      represents a specific Google    account. For example,
      `alice@example.com` .   * `serviceAccount:{emailid}`: An email address
      that represents a service    account. For example, `my-other-
      app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address
      that represents a Google group.    For example, `admins@example.com`.  *
      `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique
      identifier) representing a user that has been recently deleted. For
      example, `alice@example.com?uid=123456789012345678901`. If the user is
      recovered, this value reverts to `user:{emailid}` and the recovered user
      retains the role in the binding.  *
      `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address
      (plus    unique identifier) representing a service account that has been
      recently    deleted. For example,    `my-other-
      app@appspot.gserviceaccount.com?uid=123456789012345678901`.    If the
      service account is undeleted, this value reverts to
      `serviceAccount:{emailid}` and the undeleted service account retains the
      role in the binding.  * `deleted:group:{emailid}?uid={uniqueid}`: An
      email address (plus unique    identifier) representing a Google group
      that has been recently    deleted. For example,
      `admins@example.com?uid=123456789012345678901`. If    the group is
      recovered, this value reverts to `group:{emailid}` and the    recovered
      group retains the role in the binding.   * `domain:{domain}`: The G
      Suite domain (primary) that represents all the    users of that domain.
      For example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`.
  """

  condition = _messages.MessageField('Expr', 1)
  members = _messages.StringField(2, repeated=True)
  role = _messages.StringField(3)


class Brand(_messages.Message):
  r"""OAuth brand data. NOTE: Only contains a portion of the data that
  describes a brand.

  Fields:
    applicationTitle: Application name displayed on OAuth consent screen.
    name: Output only. Identifier of the brand. NOTE: GCP project number
      achieves the same brand identification purpose as only one brand per
      project can be created.
    orgInternalOnly: Output only. Whether the brand is only intended for usage
      inside the GSuite organization only.
    supportEmail: Support email displayed on the OAuth consent screen.
  """

  applicationTitle = _messages.StringField(1)
  name = _messages.StringField(2)
  orgInternalOnly = _messages.BooleanField(3)
  supportEmail = _messages.StringField(4)


class CorsSettings(_messages.Message):
  r"""Allows customers to configure HTTP request paths that'll allow HTTP
  OPTIONS call to bypass authentication and authorization.

  Fields:
    allowHttpOptions: Configuration to allow HTTP OPTIONS calls to skip
      authorization. If undefined, IAP will not apply any special logic to
      OPTIONS requests.
  """

  allowHttpOptions = _messages.BooleanField(1)


class CsmSettings(_messages.Message):
  r"""Configuration for RCTokens generated for CSM workloads protected by IAP.
  RCTokens are IAP generated JWTs that can be verified at the application. The
  RCToken is primarily used for ISTIO deployments, and can be scoped to a
  single mesh by configuring the audience field accordingly

  Fields:
    rctokenAud: Audience claim set in the generated RCToken. This value is not
      validated by IAP.
  """

  rctokenAud = _messages.StringField(1)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class Expr(_messages.Message):
  r"""Represents a textual expression in the Common Expression Language (CEL)
  syntax. CEL is a C-like expression language. The syntax and semantics of CEL
  are documented at https://github.com/google/cel-spec.  Example (Comparison):
  title: "Summary size limit"     description: "Determines if a summary is
  less than 100 chars"     expression: "document.summary.size() < 100"
  Example (Equality):      title: "Requestor is owner"     description:
  "Determines if requestor is the document owner"     expression:
  "document.owner == request.auth.claims.email"  Example (Logic):      title:
  "Public documents"     description: "Determine whether the document should
  be publicly visible"     expression: "document.type != 'private' &&
  document.type != 'internal'"  Example (Data Manipulation):      title:
  "Notification string"     description: "Create a notification string with a
  timestamp."     expression: "'New message received at ' +
  string(document.create_time)"  The exact variables and functions that may be
  referenced within an expression are determined by the service that evaluates
  it. See the service documentation for additional information.

  Fields:
    description: Optional. Description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.
    location: Optional. String indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: Optional. Title for the expression, i.e. a short string describing
      its purpose. This can be used e.g. in UIs which allow to enter the
      expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class GcipSettings(_messages.Message):
  r"""Allows customers to configure tenant_id for GCIP instance per-app.

  Fields:
    loginPageUri: Login page URI associated with the GCIP tenants. Typically,
      all resources within the same project share the same login page, though
      it could be overridden at the sub resource level.
    tenantIds: GCIP tenant ids that are linked to the IAP resource. tenant_ids
      could be a string beginning with a number character to indicate
      authenticating with GCIP tenant flow, or in the format of
      _<ProjectNumber> to indicate authenticating with GCIP agent flow. If
      agent flow is used, tenant_ids should only contain one single element,
      while for tenant flow, tenant_ids can contain multiple elements.
  """

  loginPageUri = _messages.StringField(1)
  tenantIds = _messages.StringField(2, repeated=True)


class GetIamPolicyRequest(_messages.Message):
  r"""Request message for `GetIamPolicy` method.

  Fields:
    options: OPTIONAL: A `GetPolicyOptions` object for specifying options to
      `GetIamPolicy`.
  """

  options = _messages.MessageField('GetPolicyOptions', 1)


class GetPolicyOptions(_messages.Message):
  r"""Encapsulates settings provided to GetIamPolicy.

  Fields:
    requestedPolicyVersion: Optional. The policy format version to be
      returned.  Valid values are 0, 1, and 3. Requests specifying an invalid
      value will be rejected.  Requests for policies with any conditional
      bindings must specify version 3. Policies without any conditional
      bindings may specify any valid value or leave the field unset.  To learn
      which resources support conditions in their IAM policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
  """

  requestedPolicyVersion = _messages.IntegerField(1, variant=_messages.Variant.INT32)


class IapGetIamPolicyRequest(_messages.Message):
  r"""A IapGetIamPolicyRequest object.

  Fields:
    getIamPolicyRequest: A GetIamPolicyRequest resource to be passed as the
      request body.
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  getIamPolicyRequest = _messages.MessageField('GetIamPolicyRequest', 1)
  resource = _messages.StringField(2, required=True)


class IapGetIapSettingsRequest(_messages.Message):
  r"""A IapGetIapSettingsRequest object.

  Fields:
    name: Required. The resource name for which to retrieve the settings.
      Authorization: Requires the `getSettings` permission for the associated
      resource.
  """

  name = _messages.StringField(1, required=True)


class IapProjectsBrandsCreateRequest(_messages.Message):
  r"""A IapProjectsBrandsCreateRequest object.

  Fields:
    brand: A Brand resource to be passed as the request body.
    parent: Required. GCP Project number/id under which the brand is to be
      created. In the following format: projects/{project_number/id}.
  """

  brand = _messages.MessageField('Brand', 1)
  parent = _messages.StringField(2, required=True)


class IapProjectsBrandsGetRequest(_messages.Message):
  r"""A IapProjectsBrandsGetRequest object.

  Fields:
    name: Required. Name of the brand to be fetched. In the following format:
      projects/{project_number/id}/brands/{brand}.
  """

  name = _messages.StringField(1, required=True)


class IapProjectsBrandsIdentityAwareProxyClientsCreateRequest(_messages.Message):
  r"""A IapProjectsBrandsIdentityAwareProxyClientsCreateRequest object.

  Fields:
    identityAwareProxyClient: A IdentityAwareProxyClient resource to be passed
      as the request body.
    parent: Required. Path to create the client in. In the following format:
      projects/{project_number/id}/brands/{brand}. The project must belong to
      a GSuite account.
  """

  identityAwareProxyClient = _messages.MessageField('IdentityAwareProxyClient', 1)
  parent = _messages.StringField(2, required=True)


class IapProjectsBrandsIdentityAwareProxyClientsDeleteRequest(_messages.Message):
  r"""A IapProjectsBrandsIdentityAwareProxyClientsDeleteRequest object.

  Fields:
    name: Required. Name of the Identity Aware Proxy client to be deleted. In
      the following format: projects/{project_number/id}/brands/{brand}/identi
      tyAwareProxyClients/{client_id}.
  """

  name = _messages.StringField(1, required=True)


class IapProjectsBrandsIdentityAwareProxyClientsGetRequest(_messages.Message):
  r"""A IapProjectsBrandsIdentityAwareProxyClientsGetRequest object.

  Fields:
    name: Required. Name of the Identity Aware Proxy client to be fetched. In
      the following format: projects/{project_number/id}/brands/{brand}/identi
      tyAwareProxyClients/{client_id}.
  """

  name = _messages.StringField(1, required=True)


class IapProjectsBrandsIdentityAwareProxyClientsListRequest(_messages.Message):
  r"""A IapProjectsBrandsIdentityAwareProxyClientsListRequest object.

  Fields:
    pageSize: The maximum number of clients to return. The service may return
      fewer than this value. If unspecified, at most 100 clients will be
      returned. The maximum value is 1000; values above 1000 will be coerced
      to 1000.
    pageToken: A page token, received from a previous
      `ListIdentityAwareProxyClients` call. Provide this to retrieve the
      subsequent page.  When paginating, all other parameters provided to
      `ListIdentityAwareProxyClients` must match the call that provided the
      page token.
    parent: Required. Full brand path. In the following format:
      projects/{project_number/id}/brands/{brand}.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class IapProjectsBrandsIdentityAwareProxyClientsResetSecretRequest(_messages.Message):
  r"""A IapProjectsBrandsIdentityAwareProxyClientsResetSecretRequest object.

  Fields:
    name: Required. Name of the Identity Aware Proxy client to that will have
      its secret reset. In the following format: projects/{project_number/id}/
      brands/{brand}/identityAwareProxyClients/{client_id}.
    resetIdentityAwareProxyClientSecretRequest: A
      ResetIdentityAwareProxyClientSecretRequest resource to be passed as the
      request body.
  """

  name = _messages.StringField(1, required=True)
  resetIdentityAwareProxyClientSecretRequest = _messages.MessageField('ResetIdentityAwareProxyClientSecretRequest', 2)


class IapProjectsBrandsListRequest(_messages.Message):
  r"""A IapProjectsBrandsListRequest object.

  Fields:
    parent: Required. GCP Project number/id. In the following format:
      projects/{project_number/id}.
  """

  parent = _messages.StringField(1, required=True)


class IapSetIamPolicyRequest(_messages.Message):
  r"""A IapSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class IapSettings(_messages.Message):
  r"""The IAP configurable settings.

  Fields:
    accessSettings: Top level wrapper for all access related setting in IAP
    applicationSettings: Top level wrapper for all application related
      settings in IAP
    name: Required. The resource name of the IAP protected resource.
  """

  accessSettings = _messages.MessageField('AccessSettings', 1)
  applicationSettings = _messages.MessageField('ApplicationSettings', 2)
  name = _messages.StringField(3)


class IapTestIamPermissionsRequest(_messages.Message):
  r"""A IapTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class IapUpdateIapSettingsRequest(_messages.Message):
  r"""A IapUpdateIapSettingsRequest object.

  Fields:
    iapSettings: A IapSettings resource to be passed as the request body.
    name: Required. The resource name of the IAP protected resource.
    updateMask: The field mask specifying which IAP settings should be
      updated. If omitted, the all of the settings are updated. See
      https://developers.google.com/protocol-
      buffers/docs/reference/google.protobuf#fieldmask
  """

  iapSettings = _messages.MessageField('IapSettings', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class IdentityAwareProxyClient(_messages.Message):
  r"""Contains the data that describes an Identity Aware Proxy owned client.

  Fields:
    displayName: Human-friendly name given to the OAuth client.
    name: Output only. Unique identifier of the OAuth client.
    secret: Output only. Client secret of the OAuth client.
  """

  displayName = _messages.StringField(1)
  name = _messages.StringField(2)
  secret = _messages.StringField(3)


class ListBrandsResponse(_messages.Message):
  r"""Response message for ListBrands.

  Fields:
    brands: Brands existing in the project.
  """

  brands = _messages.MessageField('Brand', 1, repeated=True)


class ListIdentityAwareProxyClientsResponse(_messages.Message):
  r"""Response message for ListIdentityAwareProxyClients.

  Fields:
    identityAwareProxyClients: Clients existing in the brand.
    nextPageToken: A token, which can be send as `page_token` to retrieve the
      next page. If this field is omitted, there are no subsequent pages.
  """

  identityAwareProxyClients = _messages.MessageField('IdentityAwareProxyClient', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class OAuthSettings(_messages.Message):
  r"""Configuration for OAuth login&consent flow behavior as well as for OAuth
  Credentials.

  Fields:
    clientId: OAuth 2.0 client ID used in the OAuth flow to generate an access
      token. If this field is set, you can skip obtaining the OAuth
      credentials in this step:
      https://developers.google.com/identity/protocols/OAuth2?hl=en_US#1
      .-obtain-oauth-2.0-credentials-from-the-google-api-console. However,
      this could allow for client sharing. The risks of client sharing are
      outlined here: https://cloud.google.com/iap/docs/sharing-oauth-
      clients#risks.
    loginHint: Domain hint to send as hd=? parameter in OAuth request flow.
      Enables redirect to primary IDP by skipping Google's login screen.
      https://developers.google.com/identity/protocols/OpenIDConnect#hd-param
      Note: IAP does not verify that the id token's hd claim matches this
      value since access behavior is managed by IAM policies.
  """

  clientId = _messages.StringField(1)
  loginHint = _messages.StringField(2)


class Policy(_messages.Message):
  r"""An Identity and Access Management (IAM) policy, which specifies access
  controls for Google Cloud resources.   A `Policy` is a collection of
  `bindings`. A `binding` binds one or more `members` to a single `role`.
  Members can be user accounts, service accounts, Google groups, and domains
  (such as G Suite). A `role` is a named list of permissions; each `role` can
  be an IAM predefined role or a user-created custom role.  For some types of
  Google Cloud resources, a `binding` can also specify a `condition`, which is
  a logical expression that allows access to a resource only if the expression
  evaluates to `true`. A condition can add constraints based on attributes of
  the request, the resource, or both. To learn which resources support
  conditions in their IAM policies, see the [IAM
  documentation](https://cloud.google.com/iam/help/conditions/resource-
  policies).  **JSON example:**      {       "bindings": [         {
  "role": "roles/resourcemanager.organizationAdmin",           "members": [
  "user:mike@example.com",             "group:admins@example.com",
  "domain:google.com",             "serviceAccount:my-project-
  id@appspot.gserviceaccount.com"           ]         },         {
  "role": "roles/resourcemanager.organizationViewer",           "members": [
  "user:eve@example.com"           ],           "condition": {
  "title": "expirable access",             "description": "Does not grant
  access after Sep 2020",             "expression": "request.time <
  timestamp('2020-10-01T00:00:00.000Z')",           }         }       ],
  "etag": "BwWWja0YfJA=",       "version": 3     }  **YAML example:**
  bindings:     - members:       - user:mike@example.com       -
  group:admins@example.com       - domain:google.com       - serviceAccount
  :my-project-id@appspot.gserviceaccount.com       role:
  roles/resourcemanager.organizationAdmin     - members:       -
  user:eve@example.com       role: roles/resourcemanager.organizationViewer
  condition:         title: expirable access         description: Does not
  grant access after Sep 2020         expression: request.time <
  timestamp('2020-10-01T00:00:00.000Z')     - etag: BwWWja0YfJA=     -
  version: 3  For a description of IAM and its features, see the [IAM
  documentation](https://cloud.google.com/iam/docs/).

  Fields:
    bindings: Associates a list of `members` to a `role`. Optionally, may
      specify a `condition` that determines how and when the `bindings` are
      applied. Each of the `bindings` must contain at least one member.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy.  **Important:** If you use IAM Conditions, you must include the
      `etag` field whenever you call `setIamPolicy`. If you omit this field,
      then IAM allows you to overwrite a version `3` policy with a version `1`
      policy, and all of the conditions in the version `3` policy are lost.
    version: Specifies the format of the policy.  Valid values are `0`, `1`,
      and `3`. Requests that specify an invalid value are rejected.  Any
      operation that affects conditional role bindings must specify version
      `3`. This requirement applies to the following operations:  * Getting a
      policy that includes a conditional role binding * Adding a conditional
      role binding to a policy * Changing a conditional role binding in a
      policy * Removing any role binding, with or without a condition, from a
      policy   that includes conditions  **Important:** If you use IAM
      Conditions, you must include the `etag` field whenever you call
      `setIamPolicy`. If you omit this field, then IAM allows you to overwrite
      a version `3` policy with a version `1` policy, and all of the
      conditions in the version `3` policy are lost.  If a policy does not
      include any conditions, operations on that policy may specify any valid
      version or leave the field unset.  To learn which resources support
      conditions in their IAM policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
  """

  bindings = _messages.MessageField('Binding', 1, repeated=True)
  etag = _messages.BytesField(2)
  version = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class PolicyDelegationSettings(_messages.Message):
  r"""PolicyDelegationConfig allows google-internal teams to use IAP for apps
  hosted in a tenant project. Using these settings, the app can delegate
  permission check to happen against the linked customer project. This is only
  ever supposed to be used by google internal teams, hence the restriction on
  the proto.

  Fields:
    iamPermission: Permission to check in IAM.
    iamServiceName: The DNS name of the service (e.g.
      "resourcemanager.googleapis.com"). This should be the domain name part
      of the full resource names (see https://aip.dev/122#full-resource-
      names), which is usually the same as IamServiceSpec.service of the
      service where the resource type is defined.
    policyName: Policy name to be checked
    resource: IAM resource to check permission on
  """

  iamPermission = _messages.StringField(1)
  iamServiceName = _messages.StringField(2)
  policyName = _messages.MessageField('PolicyName', 3)
  resource = _messages.MessageField('Resource', 4)


class PolicyName(_messages.Message):
  r"""A PolicyName object.

  Fields:
    id: A string attribute.
    region: For Cloud IAM: The location of the Policy. Must be empty or
      "global" for Policies owned by global IAM.  Must name a region from
      prodspec/cloud-iam-cloudspec for Regional IAM Policies, see go/iam-faq
      #where-is-iam-currently-deployed.  For Local IAM: This field should be
      set to "local".
    type: Valid values for type might be 'gce', 'gcs', 'project', 'account'
      etc.
  """

  id = _messages.StringField(1)
  region = _messages.StringField(2)
  type = _messages.StringField(3)


class ResetIdentityAwareProxyClientSecretRequest(_messages.Message):
  r"""The request sent to ResetIdentityAwareProxyClientSecret."""


class Resource(_messages.Message):
  r"""A Resource object.

  Messages:
    LabelsValue: The service defined labels of the resource on which the
      conditions will be evaluated. The semantics - including the key names -
      are vague to IAM. If the effective condition has a reference to a
      `resource.labels[foo]` construct, IAM consults with this map to retrieve
      the values associated with `foo` key for Conditions evaluation. If the
      provided key is not found in the labels map, the condition would
      evaluate to false.  This field is in limited use. If your intended use
      case is not expected to express resource.labels attribute in IAM
      Conditions, leave this field empty. Before planning on using this
      attribute please: * Read go/iam-conditions-labels-comm and ensure your
      service can meet the   data availability and management requirements. *
      Talk to iam-conditions-eng@ about your use case.

  Fields:
    labels: The service defined labels of the resource on which the conditions
      will be evaluated. The semantics - including the key names - are vague
      to IAM. If the effective condition has a reference to a
      `resource.labels[foo]` construct, IAM consults with this map to retrieve
      the values associated with `foo` key for Conditions evaluation. If the
      provided key is not found in the labels map, the condition would
      evaluate to false.  This field is in limited use. If your intended use
      case is not expected to express resource.labels attribute in IAM
      Conditions, leave this field empty. Before planning on using this
      attribute please: * Read go/iam-conditions-labels-comm and ensure your
      service can meet the   data availability and management requirements. *
      Talk to iam-conditions-eng@ about your use case.
    name: Name of the resource on which conditions will be evaluated. Must use
      the Relative Resource Name of the resource, which is the URI path of the
      resource without the leading "/". Examples are "projects/_/buckets
      /[BUCKET-ID]" for storage buckets or "projects/[PROJECT-
      ID]/global/firewalls/[FIREWALL-ID]" for a firewall.  This field is
      required for evaluating conditions with rules on resource names. For a
      `list` permission check, the resource.name value must be set to the
      parent resource. If the parent resource is a project, this field should
      be left unset.
    service: The name of the service this resource belongs to. It is
      configured using the official_service_name of the Service as defined in
      service configurations under //configs/cloud/resourcetypes. For example,
      the official_service_name of cloud resource manager service is set as
      'cloudresourcemanager.googleapis.com' according to
      //configs/cloud/resourcetypes/google/cloud/resourcemanager/prod.yaml
    type: The public resource type name of the resource on which conditions
      will be evaluated. It is configured using the official_name of the
      ResourceType as defined in service configurations under
      //configs/cloud/resourcetypes. For example, the official_name for GCP
      projects is set as 'cloudresourcemanager.googleapis.com/Project'
      according to
      //configs/cloud/resourcetypes/google/cloud/resourcemanager/prod.yaml For
      details see go/iam-conditions-integration-guide.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""The service defined labels of the resource on which the conditions
    will be evaluated. The semantics - including the key names - are vague to
    IAM. If the effective condition has a reference to a
    `resource.labels[foo]` construct, IAM consults with this map to retrieve
    the values associated with `foo` key for Conditions evaluation. If the
    provided key is not found in the labels map, the condition would evaluate
    to false.  This field is in limited use. If your intended use case is not
    expected to express resource.labels attribute in IAM Conditions, leave
    this field empty. Before planning on using this attribute please: * Read
    go/iam-conditions-labels-comm and ensure your service can meet the   data
    availability and management requirements. * Talk to iam-conditions-eng@
    about your use case.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  labels = _messages.MessageField('LabelsValue', 1)
  name = _messages.StringField(2)
  service = _messages.StringField(3)
  type = _messages.StringField(4)


class SetIamPolicyRequest(_messages.Message):
  r"""Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Cloud Platform services (such as Projects)
      might reject them.
  """

  policy = _messages.MessageField('Policy', 1)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class TestIamPermissionsRequest(_messages.Message):
  r"""Request message for `TestIamPermissions` method.

  Fields:
    permissions: The set of permissions to check for the `resource`.
      Permissions with wildcards (such as '*' or 'storage.*') are not allowed.
      For more information see [IAM
      Overview](https://cloud.google.com/iam/docs/overview#permissions).
  """

  permissions = _messages.StringField(1, repeated=True)


class TestIamPermissionsResponse(_messages.Message):
  r"""Response message for `TestIamPermissions` method.

  Fields:
    permissions: A subset of `TestPermissionsRequest.permissions` that the
      caller is allowed.
  """

  permissions = _messages.StringField(1, repeated=True)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
