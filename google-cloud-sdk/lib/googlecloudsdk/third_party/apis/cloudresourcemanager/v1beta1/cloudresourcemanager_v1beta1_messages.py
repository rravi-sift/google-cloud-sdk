"""Generated message classes for cloudresourcemanager version v1beta1.

The Google Cloud Resource Manager API provides methods for creating, reading,
and updating of project metadata.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from protorpc import messages as _messages

from googlecloudsdk.third_party.apitools.base.py import encoding


package = 'cloudresourcemanager'


class Binding(_messages.Message):
  """Associates `members` with a `role`.

  Fields:
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following formats:  * `allUsers`: A
      special identifier that represents anyone who is    on the internet;
      with or without a Google account.  * `allAuthenticatedUsers`: A special
      identifier that represents anyone    who is authenticated with a Google
      account or a service account.  * `user:{emailid}`: An email address that
      represents a specific Google    account. For example, `alice@gmail.com`
      or `joe@example.com`.  * `serviceAccount:{emailid}`: An email address
      that represents a service    account. For example, `my-other-
      app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address
      that represents a Google group.    For example, `admins@example.com`.  *
      `domain:{domain}`: A Google Apps domain name that represents all the
      users of that domain. For example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`. Required
  """

  members = _messages.StringField(1, repeated=True)
  role = _messages.StringField(2)


class CloudresourcemanagerOrganizationsGetIamPolicyRequest(_messages.Message):
  """A CloudresourcemanagerOrganizationsGetIamPolicyRequest object.

  Fields:
    getIamPolicyRequest: A GetIamPolicyRequest resource to be passed as the
      request body.
    resource: REQUIRED: The resource for which policy is being requested.
      `resource` is usually specified as a path, such as,
      `projects/{project}/zones/{zone}/disks/{disk}`.  The format for the path
      specified in this value is resource specific and is specified in the
      documentation for the respective GetIamPolicy rpc.
  """

  getIamPolicyRequest = _messages.MessageField('GetIamPolicyRequest', 1)
  resource = _messages.StringField(2, required=True)


class CloudresourcemanagerOrganizationsGetRequest(_messages.Message):
  """A CloudresourcemanagerOrganizationsGetRequest object.

  Fields:
    organizationId: The id of the Organization resource to fetch.
  """

  organizationId = _messages.StringField(1, required=True)


class CloudresourcemanagerOrganizationsListRequest(_messages.Message):
  """A CloudresourcemanagerOrganizationsListRequest object.

  Fields:
    filter: An optional query string used to filter the Organizations to be
      return in the response. Filter rules are case-insensitive.
      Organizations may be filtered by `owner.directoryCustomerId` or by
      `domain`, where the domain is a Google for Work domain, for example:
      |Filter|Description| |------|-----------|
      |owner.directorycustomerid:123456789|Organizations with
      `owner.directory_customer_id` equal to `123456789`.|
      |domain:google.com|Organizations corresponding to the domain
      `google.com`.|  This field is optional.
    pageSize: The maximum number of Organizations to return in the response.
      This field is optional.
    pageToken: A pagination token returned from a previous call to
      ListOrganizations that indicates from where listing should continue.
      This field is optional.
  """

  filter = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)


class CloudresourcemanagerOrganizationsSetIamPolicyRequest(_messages.Message):
  """A CloudresourcemanagerOrganizationsSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which policy is being specified.
      `resource` is usually specified as a path, such as,
      `projects/{project}/zones/{zone}/disks/{disk}`.  The format for the path
      specified in this value is resource specific and is specified in the
      documentation for the respective SetIamPolicy rpc.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class CloudresourcemanagerOrganizationsTestIamPermissionsRequest(_messages.Message):
  """A CloudresourcemanagerOrganizationsTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which policy detail is being
      requested. `resource` is usually specified as a path, such as,
      `projects/{project}/zones/{zone}/disks/{disk}`.  The format for the path
      specified in this value is resource specific and is specified in the
      documentation for the respective TestIamPermissions rpc.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class CloudresourcemanagerProjectsDeleteRequest(_messages.Message):
  """A CloudresourcemanagerProjectsDeleteRequest object.

  Fields:
    projectId: The project ID (for example, `foo-bar-123`).  Required.
  """

  projectId = _messages.StringField(1, required=True)


class CloudresourcemanagerProjectsGetIamPolicyRequest(_messages.Message):
  """A CloudresourcemanagerProjectsGetIamPolicyRequest object.

  Fields:
    getIamPolicyRequest: A GetIamPolicyRequest resource to be passed as the
      request body.
    resource: REQUIRED: The resource for which policy is being requested.
      `resource` is usually specified as a path, such as,
      `projects/{project}/zones/{zone}/disks/{disk}`.  The format for the path
      specified in this value is resource specific and is specified in the
      documentation for the respective GetIamPolicy rpc.
  """

  getIamPolicyRequest = _messages.MessageField('GetIamPolicyRequest', 1)
  resource = _messages.StringField(2, required=True)


class CloudresourcemanagerProjectsGetRequest(_messages.Message):
  """A CloudresourcemanagerProjectsGetRequest object.

  Fields:
    projectId: The project ID (for example, `my-project-123`).  Required.
  """

  projectId = _messages.StringField(1, required=True)


class CloudresourcemanagerProjectsListRequest(_messages.Message):
  """A CloudresourcemanagerProjectsListRequest object.

  Fields:
    filter: An expression for filtering the results of the request.  Filter
      rules are case insensitive. The fields eligible for filtering are:  +
      `name` + `id` + <code>labels.<em>key</em></code> where *key* is the name
      of a label  Some examples of using labels as filters:
      |Filter|Description| |------|-----------| |name:*|The project has a
      name.| |name:Howl|The project's name is `Howl` or `howl`.|
      |name:HOWL|Equivalent to above.| |NAME:howl|Equivalent to above.|
      |labels.color:*|The project has the label `color`.|
      |labels.color:red|The project's label `color` has the value `red`.|
      |labels.color:red&nbsp;label.size:big|The project's label `color` has
      the value `red` and its label `size` has the value `big`.  Optional.
    pageSize: The maximum number of Projects to return in the response. The
      server can return fewer projects than requested. If unspecified, server
      picks an appropriate default.  Optional.
    pageToken: A pagination token returned from a previous call to ListProject
      that indicates from where listing should continue.  Optional.
  """

  filter = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)


class CloudresourcemanagerProjectsSetIamPolicyRequest(_messages.Message):
  """A CloudresourcemanagerProjectsSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which policy is being specified.
      `resource` is usually specified as a path, such as,
      `projects/{project}/zones/{zone}/disks/{disk}`.  The format for the path
      specified in this value is resource specific and is specified in the
      documentation for the respective SetIamPolicy rpc.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class CloudresourcemanagerProjectsTestIamPermissionsRequest(_messages.Message):
  """A CloudresourcemanagerProjectsTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which policy detail is being
      requested. `resource` is usually specified as a path, such as,
      `projects/{project}/zones/{zone}/disks/{disk}`.  The format for the path
      specified in this value is resource specific and is specified in the
      documentation for the respective TestIamPermissions rpc.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class CloudresourcemanagerProjectsUndeleteRequest(_messages.Message):
  """A CloudresourcemanagerProjectsUndeleteRequest object.

  Fields:
    projectId: The project ID (for example, `foo-bar-123`).  Required.
  """

  projectId = _messages.StringField(1, required=True)


class Empty(_messages.Message):
  """A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class GetIamPolicyRequest(_messages.Message):
  """Request message for `GetIamPolicy` method."""


class ListOrganizationsResponse(_messages.Message):
  """The response returned from the ListOrganizations method.

  Fields:
    nextPageToken: A pagination token to be used to retrieve the next page of
      results. If the result is too large to fit within the page size
      specified in the request, this field will be set with a token that can
      be used to fetch the next page of results. If this field is empty, it
      indicates that this response contains the last page of results.
    organizations: The list of Organizations that matched the list query,
      possibly paginated.
  """

  nextPageToken = _messages.StringField(1)
  organizations = _messages.MessageField('Organization', 2, repeated=True)


class ListProjectsResponse(_messages.Message):
  """A page of the response received from the ListProjects method.  A
  paginated response where more pages are available has `next_page_token` set.
  This token can be used in a subsequent request to retrieve the next request
  page.

  Fields:
    nextPageToken: Pagination token.  If the result set is too large to fit in
      a single response, this token is returned. It encodes the position of
      the current result cursor. Feeding this value into a new list request
      with the `page_token` parameter gives the next page of the results.
      When `next_page_token` is not filled in, there is no next page and the
      list returned is the last page in the result set.  Pagination tokens
      have a limited lifetime.
    projects: The list of projects that matched the list filter. This list can
      be paginated.
  """

  nextPageToken = _messages.StringField(1)
  projects = _messages.MessageField('Project', 2, repeated=True)


class Organization(_messages.Message):
  """The root node in the resource hierarchy to which a particular entity's
  (e.g., company) resources belong.

  Fields:
    creationTime: Timestamp when the Organization was created. Assigned by the
      server. @OutputOnly
    displayName: A friendly string to be used to refer to the Organization in
      the UI. This field is required.
    organizationId: An immutable id for the Organization that is assigned on
      creation. This should be omitted when creating a new Organization. This
      field is read-only.
    owner: The owner of this Organization. The owner should be specified upon
      creation. Once set, it cannot be changed. This field is required.
  """

  creationTime = _messages.StringField(1)
  displayName = _messages.StringField(2)
  organizationId = _messages.StringField(3)
  owner = _messages.MessageField('OrganizationOwner', 4)


class OrganizationOwner(_messages.Message):
  """The entity that owns an Organization. The lifetime of the Organization
  and all of its descendants are bound to the OrganizationOwner. If the
  OrganizationOwner is deleted, the Organization and all its descendants will
  be deleted.

  Fields:
    directoryCustomerId: The Google for Work customer id used in the Directory
      API.
  """

  directoryCustomerId = _messages.StringField(1)


class Policy(_messages.Message):
  """Defines an Identity and Access Management (IAM) policy. It is used to
  specify access control policies for Cloud Platform resources.   A `Policy`
  consists of a list of `bindings`. A `Binding` binds a list of `members` to a
  `role`, where the members can be user accounts, Google groups, Google
  domains, and service accounts. A `role` is a named list of permissions
  defined by IAM.  **Example**      {         "bindings": [          {
  "role": "roles/owner",              "members": [
  "user:mike@example.com",              "group:admins@example.com",
  "domain:google.com",              "serviceAccount:my-other-
  app@appspot.gserviceaccount.com"]          },          {
  "role": "roles/viewer",              "members": ["user:sean@example.com"]
  }          ]     }  For a description of IAM and its features, see the [IAM
  developer's guide](https://cloud.google.com/iam).

  Fields:
    bindings: Associates a list of `members` to a `role`. Multiple `bindings`
      must not be specified for the same `role`. `bindings` with no members
      will result in an error.
    etag: The etag is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the etag in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: Etags are returned in the response to GetIamPolicy, and
      systems are expected to put that etag in the request to SetIamPolicy to
      ensure that their change will be applied to the same version of the
      policy.  If no etag is provided in the call to SetIamPolicy, then the
      existing policy is overwritten blindly.
    version: Version of the `Policy`. The default version is 0. 0 =
      resourcemanager_projects only support legacy roles. 1 = supports non-
      legacy roles 2 = supports AuditConfig
  """

  bindings = _messages.MessageField('Binding', 1, repeated=True)
  etag = _messages.BytesField(2)
  version = _messages.IntegerField(3, variant=_messages.Variant.INT32)


class Project(_messages.Message):
  """A Project is a high-level Google Cloud Platform entity.  It is a
  container for ACLs, APIs, AppEngine Apps, VMs, and other Google Cloud
  Platform resources.

  Enums:
    LifecycleStateValueValuesEnum: The project lifecycle state.  Read-only.

  Messages:
    LabelsValue: The labels associated with this project.  Label keys must be
      between 1 and 63 characters long and must conform to the following
      regular expression: \[a-z\](\[-a-z0-9\]*\[a-z0-9\])?.  Label values must
      be between 0 and 63 characters long and must conform to the regular
      expression (\[a-z\](\[-a-z0-9\]*\[a-z0-9\])?)?.  No more than 256 labels
      can be associated with a given resource.  Clients should store labels in
      a representation such as JSON that does not depend on specific
      characters being disallowed.  Example: <code>"environment" :
      "dev"</code>  Read-write.

  Fields:
    createTime: Creation time.  Read-only.
    labels: The labels associated with this project.  Label keys must be
      between 1 and 63 characters long and must conform to the following
      regular expression: \[a-z\](\[-a-z0-9\]*\[a-z0-9\])?.  Label values must
      be between 0 and 63 characters long and must conform to the regular
      expression (\[a-z\](\[-a-z0-9\]*\[a-z0-9\])?)?.  No more than 256 labels
      can be associated with a given resource.  Clients should store labels in
      a representation such as JSON that does not depend on specific
      characters being disallowed.  Example: <code>"environment" :
      "dev"</code>  Read-write.
    lifecycleState: The project lifecycle state.  Read-only.
    name: The user-assigned name of the project. It must be 4 to 30
      characters. Allowed characters are: lowercase and uppercase letters,
      numbers, hyphen, single-quote, double-quote, space, and exclamation
      point.  Example: <code>My Project</code>  Read-write.
    parent: An optional reference to a parent Resource.  The only supported
      parent type is "organization". Once set, the parent cannot be modified.
      Read-write.
    projectId: The unique, user-assigned ID of the project. It must be 6 to 30
      lowercase letters, digits, or hyphens. It must start with a letter.
      Trailing hyphens are prohibited.  Example: <code>tokyo-rain-123</code>
      Read-only after creation.
    projectNumber: The number uniquely identifying the project.  Example:
      <code>415104041262</code>  Read-only.
  """

  class LifecycleStateValueValuesEnum(_messages.Enum):
    """The project lifecycle state.  Read-only.

    Values:
      LIFECYCLE_STATE_UNSPECIFIED: Unspecified state.  This is only
        used/useful for distinguishing unset values.
      ACTIVE: The normal and active state.
      DELETE_REQUESTED: The project has been marked for deletion by the user
        (by invoking DeleteProject) or by the system (Google Cloud Platform).
        This can generally be reversed by invoking UndeleteProject.
      DELETE_IN_PROGRESS: The process of deleting the project has begun.
        Reversing the deletion is no longer possible.
    """
    LIFECYCLE_STATE_UNSPECIFIED = 0
    ACTIVE = 1
    DELETE_REQUESTED = 2
    DELETE_IN_PROGRESS = 3

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    """The labels associated with this project.  Label keys must be between 1
    and 63 characters long and must conform to the following regular
    expression: \[a-z\](\[-a-z0-9\]*\[a-z0-9\])?.  Label values must be
    between 0 and 63 characters long and must conform to the regular
    expression (\[a-z\](\[-a-z0-9\]*\[a-z0-9\])?)?.  No more than 256 labels
    can be associated with a given resource.  Clients should store labels in a
    representation such as JSON that does not depend on specific characters
    being disallowed.  Example: <code>"environment" : "dev"</code>  Read-
    write.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  createTime = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  lifecycleState = _messages.EnumField('LifecycleStateValueValuesEnum', 3)
  name = _messages.StringField(4)
  parent = _messages.MessageField('ResourceId', 5)
  projectId = _messages.StringField(6)
  projectNumber = _messages.IntegerField(7)


class ResourceId(_messages.Message):
  """A container to reference an id for any resource type. A 'resource' in
  Google Cloud Platform is a generic term for something you (a developer) may
  want to interact with through one of our API's. Some examples are an
  AppEngine app, a Compute Engine instance, Cloud SQL database, ...

  Fields:
    id: Required field for the type-specific id. This should correspond to the
      id used in the type-specific API's.
    type: Required field representing the resource type this id is for. At
      present, the only valid type is "organization".
  """

  id = _messages.StringField(1)
  type = _messages.StringField(2)


class SetIamPolicyRequest(_messages.Message):
  """Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Cloud Platform services (such as Projects)
      might reject them.
  """

  policy = _messages.MessageField('Policy', 1)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" or "email:<ldap>" to
      include in api requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class TestIamPermissionsRequest(_messages.Message):
  """Request message for `TestIamPermissions` method.

  Fields:
    permissions: The set of permissions to check for the `resource`.
      Permissions with wildcards (such as '*' or 'storage.*') are not allowed.
  """

  permissions = _messages.StringField(1, repeated=True)


class TestIamPermissionsResponse(_messages.Message):
  """Response message for `TestIamPermissions` method.

  Fields:
    permissions: A subset of `TestPermissionsRequest.permissions` that the
      caller is allowed.
  """

  permissions = _messages.StringField(1, repeated=True)


encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1',
    package=u'cloudresourcemanager')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2',
    package=u'cloudresourcemanager')
encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv',
    package=u'cloudresourcemanager')
