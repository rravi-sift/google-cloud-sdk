"""Generated message classes for cloudbilling version v1.

Allows developers to manage billing for their Google Cloud Platform projects
programmatically.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'cloudbilling'


class AggregationInfo(_messages.Message):
  r"""Represents the aggregation level and interval for pricing of a single
  SKU.

  Enums:
    AggregationIntervalValueValuesEnum:
    AggregationLevelValueValuesEnum:

  Fields:
    aggregationCount: The number of intervals to aggregate over. Example: If
      aggregation_level is "DAILY" and aggregation_count is 14, aggregation
      will be over 14 days.
    aggregationInterval: A AggregationIntervalValueValuesEnum attribute.
    aggregationLevel: A AggregationLevelValueValuesEnum attribute.
  """

  class AggregationIntervalValueValuesEnum(_messages.Enum):
    r"""AggregationIntervalValueValuesEnum enum type.

    Values:
      AGGREGATION_INTERVAL_UNSPECIFIED: <no description>
      DAILY: <no description>
      MONTHLY: <no description>
    """
    AGGREGATION_INTERVAL_UNSPECIFIED = 0
    DAILY = 1
    MONTHLY = 2

  class AggregationLevelValueValuesEnum(_messages.Enum):
    r"""AggregationLevelValueValuesEnum enum type.

    Values:
      AGGREGATION_LEVEL_UNSPECIFIED: <no description>
      ACCOUNT: <no description>
      PROJECT: <no description>
    """
    AGGREGATION_LEVEL_UNSPECIFIED = 0
    ACCOUNT = 1
    PROJECT = 2

  aggregationCount = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  aggregationInterval = _messages.EnumField('AggregationIntervalValueValuesEnum', 2)
  aggregationLevel = _messages.EnumField('AggregationLevelValueValuesEnum', 3)


class AuditConfig(_messages.Message):
  r"""Specifies the audit configuration for a service. The configuration
  determines which permission types are logged, and what identities, if any,
  are exempted from logging. An AuditConfig must have one or more
  AuditLogConfigs.  If there are AuditConfigs for both `allServices` and a
  specific service, the union of the two AuditConfigs is used for that
  service: the log_types specified in each AuditConfig are enabled, and the
  exempted_members in each AuditLogConfig are exempted.  Example Policy with
  multiple AuditConfigs:      {       "audit_configs": [         {
  "service": "allServices"           "audit_log_configs": [             {
  "log_type": "DATA_READ",               "exempted_members": [
  "user:jose@example.com"               ]             },             {
  "log_type": "DATA_WRITE",             },             {
  "log_type": "ADMIN_READ",             }           ]         },         {
  "service": "sampleservice.googleapis.com"           "audit_log_configs": [
  {               "log_type": "DATA_READ",             },             {
  "log_type": "DATA_WRITE",               "exempted_members": [
  "user:aliya@example.com"               ]             }           ]         }
  ]     }  For sampleservice, this policy enables DATA_READ, DATA_WRITE and
  ADMIN_READ logging. It also exempts jose@example.com from DATA_READ logging,
  and aliya@example.com from DATA_WRITE logging.

  Fields:
    auditLogConfigs: The configuration for logging of each type of permission.
    service: Specifies a service that will be enabled for audit logging. For
      example, `storage.googleapis.com`, `cloudsql.googleapis.com`.
      `allServices` is a special value that covers all services.
  """

  auditLogConfigs = _messages.MessageField('AuditLogConfig', 1, repeated=True)
  service = _messages.StringField(2)


class AuditLogConfig(_messages.Message):
  r"""Provides the configuration for logging a type of permissions. Example:
  {       "audit_log_configs": [         {           "log_type": "DATA_READ",
  "exempted_members": [             "user:jose@example.com"           ]
  },         {           "log_type": "DATA_WRITE",         }       ]     }
  This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting
  jose@example.com from DATA_READ logging.

  Enums:
    LogTypeValueValuesEnum: The log type that this config enables.

  Fields:
    exemptedMembers: Specifies the identities that do not cause logging for
      this type of permission. Follows the same format of Binding.members.
    logType: The log type that this config enables.
  """

  class LogTypeValueValuesEnum(_messages.Enum):
    r"""The log type that this config enables.

    Values:
      LOG_TYPE_UNSPECIFIED: Default case. Should never be this.
      ADMIN_READ: Admin reads. Example: CloudIAM getIamPolicy
      DATA_WRITE: Data writes. Example: CloudSQL Users create
      DATA_READ: Data reads. Example: CloudSQL Users list
    """
    LOG_TYPE_UNSPECIFIED = 0
    ADMIN_READ = 1
    DATA_WRITE = 2
    DATA_READ = 3

  exemptedMembers = _messages.StringField(1, repeated=True)
  logType = _messages.EnumField('LogTypeValueValuesEnum', 2)


class BillingAccount(_messages.Message):
  r"""A billing account in [GCP Console](https://console.cloud.google.com/).
  You can assign a billing account to one or more projects.

  Fields:
    displayName: The display name given to the billing account, such as `My
      Billing Account`. This name is displayed in the GCP Console.
    masterBillingAccount: If this account is a
      [subaccount](https://cloud.google.com/billing/docs/concepts), then this
      will be the resource name of the master billing account that it is being
      resold through. Otherwise this will be empty.
    name: The resource name of the billing account. The resource name has the
      form `billingAccounts/{billing_account_id}`. For example,
      `billingAccounts/012345-567890-ABCDEF` would be the resource name for
      billing account `012345-567890-ABCDEF`.
    open: Output only. True if the billing account is open, and will therefore
      be charged for any usage on associated projects. False if the billing
      account is closed, and therefore projects associated with it will be
      unable to use paid services.
  """

  displayName = _messages.StringField(1)
  masterBillingAccount = _messages.StringField(2)
  name = _messages.StringField(3)
  open = _messages.BooleanField(4)


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


class Category(_messages.Message):
  r"""Represents the category hierarchy of a SKU.

  Fields:
    resourceFamily: The type of product the SKU refers to. Example: "Compute",
      "Storage", "Network", "ApplicationServices" etc.
    resourceGroup: A group classification for related SKUs. Example: "RAM",
      "GPU", "Prediction", "Ops", "GoogleEgress" etc.
    serviceDisplayName: The display name of the service this SKU belongs to.
    usageType: Represents how the SKU is consumed. Example: "OnDemand",
      "Preemptible", "Commit1Mo", "Commit1Yr" etc.
  """

  resourceFamily = _messages.StringField(1)
  resourceGroup = _messages.StringField(2)
  serviceDisplayName = _messages.StringField(3)
  usageType = _messages.StringField(4)


class CloudbillingBillingAccountsGetIamPolicyRequest(_messages.Message):
  r"""A CloudbillingBillingAccountsGetIamPolicyRequest object.

  Fields:
    options_requestedPolicyVersion: Optional. The policy format version to be
      returned.  Valid values are 0, 1, and 3. Requests specifying an invalid
      value will be rejected.  Requests for policies with any conditional
      bindings must specify version 3. Policies without any conditional
      bindings may specify any valid value or leave the field unset.  To learn
      which resources support conditions in their IAM policies, see the [IAM
      documentation](https://cloud.google.com/iam/help/conditions/resource-
      policies).
    resource: REQUIRED: The resource for which the policy is being requested.
      See the operation documentation for the appropriate value for this
      field.
  """

  options_requestedPolicyVersion = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  resource = _messages.StringField(2, required=True)


class CloudbillingBillingAccountsGetRequest(_messages.Message):
  r"""A CloudbillingBillingAccountsGetRequest object.

  Fields:
    name: Required. The resource name of the billing account to retrieve. For
      example, `billingAccounts/012345-567890-ABCDEF`.
  """

  name = _messages.StringField(1, required=True)


class CloudbillingBillingAccountsListRequest(_messages.Message):
  r"""A CloudbillingBillingAccountsListRequest object.

  Fields:
    filter: Options for how to filter the returned billing accounts. Currently
      this only supports filtering for
      [subaccounts](https://cloud.google.com/billing/docs/concepts) under a
      single provided reseller billing account. (e.g.
      "master_billing_account=billingAccounts/012345-678901-ABCDEF"). Boolean
      algebra and other fields are not currently supported.
    pageSize: Requested page size. The maximum page size is 100; this is also
      the default.
    pageToken: A token identifying a page of results to return. This should be
      a `next_page_token` value returned from a previous `ListBillingAccounts`
      call. If unspecified, the first page of results is returned.
  """

  filter = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)


class CloudbillingBillingAccountsPatchRequest(_messages.Message):
  r"""A CloudbillingBillingAccountsPatchRequest object.

  Fields:
    billingAccount: A BillingAccount resource to be passed as the request
      body.
    name: Required. The name of the billing account resource to be updated.
    updateMask: The update mask applied to the resource. Only "display_name"
      is currently supported.
  """

  billingAccount = _messages.MessageField('BillingAccount', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class CloudbillingBillingAccountsProjectsListRequest(_messages.Message):
  r"""A CloudbillingBillingAccountsProjectsListRequest object.

  Fields:
    name: Required. The resource name of the billing account associated with
      the projects that you want to list. For example,
      `billingAccounts/012345-567890-ABCDEF`.
    pageSize: Requested page size. The maximum page size is 100; this is also
      the default.
    pageToken: A token identifying a page of results to be returned. This
      should be a `next_page_token` value returned from a previous
      `ListProjectBillingInfo` call. If unspecified, the first page of results
      is returned.
  """

  name = _messages.StringField(1, required=True)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)


class CloudbillingBillingAccountsSetIamPolicyRequest(_messages.Message):
  r"""A CloudbillingBillingAccountsSetIamPolicyRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy is being specified.
      See the operation documentation for the appropriate value for this
      field.
    setIamPolicyRequest: A SetIamPolicyRequest resource to be passed as the
      request body.
  """

  resource = _messages.StringField(1, required=True)
  setIamPolicyRequest = _messages.MessageField('SetIamPolicyRequest', 2)


class CloudbillingBillingAccountsTestIamPermissionsRequest(_messages.Message):
  r"""A CloudbillingBillingAccountsTestIamPermissionsRequest object.

  Fields:
    resource: REQUIRED: The resource for which the policy detail is being
      requested. See the operation documentation for the appropriate value for
      this field.
    testIamPermissionsRequest: A TestIamPermissionsRequest resource to be
      passed as the request body.
  """

  resource = _messages.StringField(1, required=True)
  testIamPermissionsRequest = _messages.MessageField('TestIamPermissionsRequest', 2)


class CloudbillingProjectsGetBillingInfoRequest(_messages.Message):
  r"""A CloudbillingProjectsGetBillingInfoRequest object.

  Fields:
    name: Required. The resource name of the project for which billing
      information is retrieved. For example, `projects/tokyo-rain-123`.
  """

  name = _messages.StringField(1, required=True)


class CloudbillingProjectsUpdateBillingInfoRequest(_messages.Message):
  r"""A CloudbillingProjectsUpdateBillingInfoRequest object.

  Fields:
    name: Required. The resource name of the project associated with the
      billing information that you want to update. For example, `projects
      /tokyo-rain-123`.
    projectBillingInfo: A ProjectBillingInfo resource to be passed as the
      request body.
  """

  name = _messages.StringField(1, required=True)
  projectBillingInfo = _messages.MessageField('ProjectBillingInfo', 2)


class CloudbillingServicesListRequest(_messages.Message):
  r"""A CloudbillingServicesListRequest object.

  Fields:
    pageSize: Requested page size. Defaults to 5000.
    pageToken: A token identifying a page of results to return. This should be
      a `next_page_token` value returned from a previous `ListServices` call.
      If unspecified, the first page of results is returned.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)


class CloudbillingServicesSkusListRequest(_messages.Message):
  r"""A CloudbillingServicesSkusListRequest object.

  Fields:
    currencyCode: The ISO 4217 currency code for the pricing info in the
      response proto. Will use the conversion rate as of start_time. Optional.
      If not specified USD will be used.
    endTime: Optional exclusive end time of the time range for which the
      pricing versions will be returned. Timestamps in the future are not
      allowed. The time range has to be within a single calendar month in
      America/Los_Angeles timezone. Time range as a whole is optional. If not
      specified, the latest pricing will be returned (up to 12 hours old at
      most).
    pageSize: Requested page size. Defaults to 5000.
    pageToken: A token identifying a page of results to return. This should be
      a `next_page_token` value returned from a previous `ListSkus` call. If
      unspecified, the first page of results is returned.
    parent: Required. The name of the service. Example:
      "services/DA34-426B-A397"
    startTime: Optional inclusive start time of the time range for which the
      pricing versions will be returned. Timestamps in the future are not
      allowed. The time range has to be within a single calendar month in
      America/Los_Angeles timezone. Time range as a whole is optional. If not
      specified, the latest pricing will be returned (up to 12 hours old at
      most).
  """

  currencyCode = _messages.StringField(1)
  endTime = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  parent = _messages.StringField(5, required=True)
  startTime = _messages.StringField(6)


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


class ListBillingAccountsResponse(_messages.Message):
  r"""Response message for `ListBillingAccounts`.

  Fields:
    billingAccounts: A list of billing accounts.
    nextPageToken: A token to retrieve the next page of results. To retrieve
      the next page, call `ListBillingAccounts` again with the `page_token`
      field set to this value. This field is empty if there are no more
      results to retrieve.
  """

  billingAccounts = _messages.MessageField('BillingAccount', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListProjectBillingInfoResponse(_messages.Message):
  r"""Request message for `ListProjectBillingInfoResponse`.

  Fields:
    nextPageToken: A token to retrieve the next page of results. To retrieve
      the next page, call `ListProjectBillingInfo` again with the `page_token`
      field set to this value. This field is empty if there are no more
      results to retrieve.
    projectBillingInfo: A list of `ProjectBillingInfo` resources representing
      the projects associated with the billing account.
  """

  nextPageToken = _messages.StringField(1)
  projectBillingInfo = _messages.MessageField('ProjectBillingInfo', 2, repeated=True)


class ListServicesResponse(_messages.Message):
  r"""Response message for `ListServices`.

  Fields:
    nextPageToken: A token to retrieve the next page of results. To retrieve
      the next page, call `ListServices` again with the `page_token` field set
      to this value. This field is empty if there are no more results to
      retrieve.
    services: A list of services.
  """

  nextPageToken = _messages.StringField(1)
  services = _messages.MessageField('Service', 2, repeated=True)


class ListSkusResponse(_messages.Message):
  r"""Response message for `ListSkus`.

  Fields:
    nextPageToken: A token to retrieve the next page of results. To retrieve
      the next page, call `ListSkus` again with the `page_token` field set to
      this value. This field is empty if there are no more results to
      retrieve.
    skus: The list of public SKUs of the given service.
  """

  nextPageToken = _messages.StringField(1)
  skus = _messages.MessageField('Sku', 2, repeated=True)


class Money(_messages.Message):
  r"""Represents an amount of money with its currency type.

  Fields:
    currencyCode: The 3-letter currency code defined in ISO 4217.
    nanos: Number of nano (10^-9) units of the amount. The value must be
      between -999,999,999 and +999,999,999 inclusive. If `units` is positive,
      `nanos` must be positive or zero. If `units` is zero, `nanos` can be
      positive, zero, or negative. If `units` is negative, `nanos` must be
      negative or zero. For example $-1.75 is represented as `units`=-1 and
      `nanos`=-750,000,000.
    units: The whole units of the amount. For example if `currencyCode` is
      `"USD"`, then 1 unit is one US dollar.
  """

  currencyCode = _messages.StringField(1)
  nanos = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  units = _messages.IntegerField(3)


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
    auditConfigs: Specifies cloud audit logging configuration for this policy.
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

  auditConfigs = _messages.MessageField('AuditConfig', 1, repeated=True)
  bindings = _messages.MessageField('Binding', 2, repeated=True)
  etag = _messages.BytesField(3)
  version = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class PricingExpression(_messages.Message):
  r"""Expresses a mathematical pricing formula. For Example:-  `usage_unit:
  GBy` `tiered_rates:`    `[start_usage_amount: 20, unit_price: $10]`
  `[start_usage_amount: 100, unit_price: $5]`  The above expresses a pricing
  formula where the first 20GB is free, the next 80GB is priced at $10 per GB
  followed by $5 per GB for additional usage.

  Fields:
    baseUnit: The base unit for the SKU which is the unit used in usage
      exports. Example: "By"
    baseUnitConversionFactor: Conversion factor for converting from price per
      usage_unit to price per base_unit, and start_usage_amount to
      start_usage_amount in base_unit. unit_price /
      base_unit_conversion_factor = price per base_unit. start_usage_amount *
      base_unit_conversion_factor = start_usage_amount in base_unit.
    baseUnitDescription: The base unit in human readable form. Example:
      "byte".
    displayQuantity: The recommended quantity of units for displaying pricing
      info. When displaying pricing info it is recommended to display:
      (unit_price * display_quantity) per display_quantity usage_unit. This
      field does not affect the pricing formula and is for display purposes
      only. Example: If the unit_price is "0.0001 USD", the usage_unit is "GB"
      and the display_quantity is "1000" then the recommended way of
      displaying the pricing info is "0.10 USD per 1000 GB"
    tieredRates: The list of tiered rates for this pricing. The total cost is
      computed by applying each of the tiered rates on usage. This repeated
      list is sorted by ascending order of start_usage_amount.
    usageUnit: The short hand for unit of usage this pricing is specified in.
      Example: usage_unit of "GiBy" means that usage is specified in "Gibi
      Byte".
    usageUnitDescription: The unit of usage in human readable form. Example:
      "gibi byte".
  """

  baseUnit = _messages.StringField(1)
  baseUnitConversionFactor = _messages.FloatField(2)
  baseUnitDescription = _messages.StringField(3)
  displayQuantity = _messages.FloatField(4)
  tieredRates = _messages.MessageField('TierRate', 5, repeated=True)
  usageUnit = _messages.StringField(6)
  usageUnitDescription = _messages.StringField(7)


class PricingInfo(_messages.Message):
  r"""Represents the pricing information for a SKU at a single point of time.

  Fields:
    aggregationInfo: Aggregation Info. This can be left unspecified if the
      pricing expression doesn't require aggregation.
    currencyConversionRate: Conversion rate used for currency conversion, from
      USD to the currency specified in the request. This includes any
      surcharge collected for billing in non USD currency. If a currency is
      not specified in the request this defaults to 1.0. Example: USD *
      currency_conversion_rate = JPY
    effectiveTime: The timestamp from which this pricing was effective within
      the requested time range. This is guaranteed to be greater than or equal
      to the start_time field in the request and less than the end_time field
      in the request. If a time range was not specified in the request this
      field will be equivalent to a time within the last 12 hours, indicating
      the latest pricing info.
    pricingExpression: Expresses the pricing formula. See `PricingExpression`
      for an example.
    summary: An optional human readable summary of the pricing information,
      has a maximum length of 256 characters.
  """

  aggregationInfo = _messages.MessageField('AggregationInfo', 1)
  currencyConversionRate = _messages.FloatField(2)
  effectiveTime = _messages.StringField(3)
  pricingExpression = _messages.MessageField('PricingExpression', 4)
  summary = _messages.StringField(5)


class ProjectBillingInfo(_messages.Message):
  r"""Encapsulation of billing information for a GCP Console project. A
  project has at most one associated billing account at a time (but a billing
  account can be assigned to multiple projects).

  Fields:
    billingAccountName: The resource name of the billing account associated
      with the project, if any. For example,
      `billingAccounts/012345-567890-ABCDEF`.
    billingEnabled: True if the project is associated with an open billing
      account, to which usage on the project is charged. False if the project
      is associated with a closed billing account, or no billing account at
      all, and therefore cannot use paid services. This field is read-only.
    name: The resource name for the `ProjectBillingInfo`; has the form
      `projects/{project_id}/billingInfo`. For example, the resource name for
      the billing information for project `tokyo-rain-123` would be `projects
      /tokyo-rain-123/billingInfo`. This field is read-only.
    projectId: The ID of the project that this `ProjectBillingInfo`
      represents, such as `tokyo-rain-123`. This is a convenience field so
      that you don't need to parse the `name` field to obtain a project ID.
      This field is read-only.
  """

  billingAccountName = _messages.StringField(1)
  billingEnabled = _messages.BooleanField(2)
  name = _messages.StringField(3)
  projectId = _messages.StringField(4)


class Service(_messages.Message):
  r"""Encapsulates a single service in Google Cloud Platform.

  Fields:
    businessEntityName: The business under which the service is offered. Ex.
      "businessEntities/GCP", "businessEntities/Maps"
    displayName: A human readable display name for this service.
    name: The resource name for the service. Example:
      "services/DA34-426B-A397"
    serviceId: The identifier for the service. Example: "DA34-426B-A397"
  """

  businessEntityName = _messages.StringField(1)
  displayName = _messages.StringField(2)
  name = _messages.StringField(3)
  serviceId = _messages.StringField(4)


class SetIamPolicyRequest(_messages.Message):
  r"""Request message for `SetIamPolicy` method.

  Fields:
    policy: REQUIRED: The complete policy to be applied to the `resource`. The
      size of the policy is limited to a few 10s of KB. An empty policy is a
      valid policy but certain Cloud Platform services (such as Projects)
      might reject them.
    updateMask: OPTIONAL: A FieldMask specifying which fields of the policy to
      modify. Only the fields in the mask will be modified. If no mask is
      provided, the following default mask is used:  `paths: "bindings, etag"`
  """

  policy = _messages.MessageField('Policy', 1)
  updateMask = _messages.StringField(2)


class Sku(_messages.Message):
  r"""Encapsulates a single SKU in Google Cloud Platform

  Fields:
    category: The category hierarchy of this SKU, purely for organizational
      purpose.
    description: A human readable description of the SKU, has a maximum length
      of 256 characters.
    name: The resource name for the SKU. Example:
      "services/DA34-426B-A397/skus/AA95-CD31-42FE"
    pricingInfo: A timeline of pricing info for this SKU in chronological
      order.
    serviceProviderName: Identifies the service provider. This is 'Google' for
      first party services in Google Cloud Platform.
    serviceRegions: List of service regions this SKU is offered at. Example:
      "asia-east1" Service regions can be found at
      https://cloud.google.com/about/locations/
    skuId: The identifier for the SKU. Example: "AA95-CD31-42FE"
  """

  category = _messages.MessageField('Category', 1)
  description = _messages.StringField(2)
  name = _messages.StringField(3)
  pricingInfo = _messages.MessageField('PricingInfo', 4, repeated=True)
  serviceProviderName = _messages.StringField(5)
  serviceRegions = _messages.StringField(6, repeated=True)
  skuId = _messages.StringField(7)


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


class TierRate(_messages.Message):
  r"""The price rate indicating starting usage and its corresponding price.

  Fields:
    startUsageAmount: Usage is priced at this rate only after this amount.
      Example: start_usage_amount of 10 indicates that the usage will be
      priced at the unit_price after the first 10 usage_units.
    unitPrice: The price per unit of usage. Example: unit_price of amount $10
      indicates that each unit will cost $10.
  """

  startUsageAmount = _messages.FloatField(1)
  unitPrice = _messages.MessageField('Money', 2)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
