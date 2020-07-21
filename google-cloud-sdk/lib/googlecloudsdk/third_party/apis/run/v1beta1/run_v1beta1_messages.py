"""Generated message classes for run version v1beta1.

Deploy and manage user provided container images that scale automatically
based on HTTP traffic.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'run'


class CustomResourceColumnDefinition(_messages.Message):
  r"""CustomResourceColumnDefinition specifies a column for server side
  printing.

  Fields:
    description: description is a human readable description of this column.
      +optional
    format: format is an optional OpenAPI type definition for this column. The
      'name' format is applied to the primary identifier column to assist in
      clients identifying column is the resource name. See
      https://github.com/OAI/OpenAPI-
      Specification/blob/master/versions/2.0.md#data-types for more. +optional
    jsonPath: JSONPath is a simple JSON path, i.e. with array notation.
    name: name is a human readable name for the column.
    priority: priority is an integer defining the relative importance of this
      column compared to others. Lower numbers are considered higher priority.
      Columns that may be omitted in limited space scenarios should be given a
      higher priority. +optional
    type: type is an OpenAPI type definition for this column. See
      https://github.com/OAI/OpenAPI-
      Specification/blob/master/versions/2.0.md#data-types for more.
  """

  description = _messages.StringField(1)
  format = _messages.StringField(2)
  jsonPath = _messages.StringField(3)
  name = _messages.StringField(4)
  priority = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  type = _messages.StringField(6)


class CustomResourceDefinition(_messages.Message):
  r"""CustomResourceDefinition represents a resource that should be exposed on
  the API server.  Its name MUST be in the format <.spec.name>.<.spec.group>.

  Fields:
    apiVersion: The API version for this call such as
      "k8s.apiextensions.io/v1beta1".
    kind: The kind of resource, in this case always
      "CustomResourceDefinition".
    metadata: Metadata associated with this CustomResourceDefinition.
    spec: Spec describes how the user wants the resources to appear
  """

  apiVersion = _messages.StringField(1)
  kind = _messages.StringField(2)
  metadata = _messages.MessageField('ObjectMeta', 3)
  spec = _messages.MessageField('CustomResourceDefinitionSpec', 4)


class CustomResourceDefinitionNames(_messages.Message):
  r"""CustomResourceDefinitionNames indicates the names to serve this
  CustomResourceDefinition

  Fields:
    categories: Categories is a list of grouped resources custom resources
      belong to (e.g. 'all') +optional
    kind: Kind is the serialized kind of the resource.  It is normally
      CamelCase and singular.
    listKind: ListKind is the serialized kind of the list for this resource.
      Defaults to <kind>List. +optional
    plural: Plural is the plural name of the resource to serve.  It must match
      the name of the CustomResourceDefinition-registration too: plural.group
      and it must be all lowercase.
    shortNames: ShortNames are short names for the resource.  It must be all
      lowercase. +optional
    singular: Singular is the singular name of the resource.  It must be all
      lowercase Defaults to lowercased <kind> +optional
  """

  categories = _messages.StringField(1, repeated=True)
  kind = _messages.StringField(2)
  listKind = _messages.StringField(3)
  plural = _messages.StringField(4)
  shortNames = _messages.StringField(5, repeated=True)
  singular = _messages.StringField(6)


class CustomResourceDefinitionSpec(_messages.Message):
  r"""CustomResourceDefinitionSpec describes how a user wants their resource
  to appear

  Fields:
    additionalPrinterColumns: AdditionalPrinterColumns are additional columns
      shown e.g. in kubectl next to the name. Defaults to a created-at column.
      +optional
    group: Group is the group this resource belongs in
    names: Names are the names used to describe this custom resource
    scope: Scope indicates whether this resource is cluster or namespace
      scoped. Default is namespaced
    subresources: Subresources describes the subresources for CustomResources
      +optional
    validation: Validation describes the validation methods for
      CustomResources +optional
    version: Version is the version this resource belongs in Should be always
      first item in Versions field if provided. Optional, but at least one of
      Version or Versions must be set. Deprecated: Please use `Versions`.
      +optional
    versions: Versions is the list of all supported versions for this
      resource. If Version field is provided, this field is optional.
      Validation: All versions must use the same validation schema for now.
      i.e., top level Validation field is applied to all of these versions.
      Order: The version name will be used to compute the order. If the
      version string is "kube-like", it will sort above non "kube-like"
      version strings, which are ordered lexicographically. "Kube-like"
      versions start with a "v", then are followed by a number (the major
      version), then optionally the string "alpha" or "beta" and another
      number (the minor version). These are sorted first by GA > beta > alpha
      (where GA is a version with no suffix such as beta or alpha), and then
      by comparing major version, then minor version. An example sorted list
      of versions: v10, v2, v1, v11beta2, v10beta3, v3beta1, v12alpha1,
      v11alpha2, foo1, foo10. +optional
  """

  additionalPrinterColumns = _messages.MessageField('CustomResourceColumnDefinition', 1, repeated=True)
  group = _messages.StringField(2)
  names = _messages.MessageField('CustomResourceDefinitionNames', 3)
  scope = _messages.StringField(4)
  subresources = _messages.MessageField('CustomResourceSubresources', 5)
  validation = _messages.MessageField('CustomResourceValidation', 6)
  version = _messages.StringField(7)
  versions = _messages.MessageField('CustomResourceDefinitionVersion', 8, repeated=True)


class CustomResourceDefinitionVersion(_messages.Message):
  r"""A CustomResourceDefinitionVersion object.

  Fields:
    name: Name is the version name, e.g. "v1", "v2beta1", etc.
    served: Served is a flag enabling/disabling this version from being served
      via REST APIs
    storage: Storage flags the version as storage version. There must be
      exactly one flagged as storage version.
  """

  name = _messages.StringField(1)
  served = _messages.BooleanField(2)
  storage = _messages.BooleanField(3)


class CustomResourceSubresourceScale(_messages.Message):
  r"""CustomResourceSubresourceScale defines how to serve the scale
  subresource for CustomResources.

  Fields:
    labelSelectorPath: LabelSelectorPath defines the JSON path inside of a
      CustomResource that corresponds to Scale.Status.Selector. Only JSON
      paths without the array notation are allowed. Must be a JSON Path under
      .status. Must be set to work with HPA. If there is no value under the
      given path in the CustomResource, the status label selector value in the
      /scale subresource will default to the empty string. +optional
    specReplicasPath: SpecReplicasPath defines the JSON path inside of a
      CustomResource that corresponds to Scale.Spec.Replicas. Only JSON paths
      without the array notation are allowed. Must be a JSON Path under .spec.
      If there is no value under the given path in the CustomResource, the
      /scale subresource will return an error on GET.
    statusReplicasPath: StatusReplicasPath defines the JSON path inside of a
      CustomResource that corresponds to Scale.Status.Replicas. Only JSON
      paths without the array notation are allowed. Must be a JSON Path under
      .status. If there is no value under the given path in the
      CustomResource, the status replica value in the /scale subresource will
      default to 0.
  """

  labelSelectorPath = _messages.StringField(1)
  specReplicasPath = _messages.StringField(2)
  statusReplicasPath = _messages.StringField(3)


class CustomResourceSubresourceStatus(_messages.Message):
  r"""CustomResourceSubresourceStatus defines how to serve the status
  subresource for CustomResources. Status is represented by the `.status` JSON
  path inside of a CustomResource. When set, * exposes a /status subresource
  for the custom resource * PUT requests to the /status subresource take a
  custom resource object, and ignore changes to anything except the status
  stanza * PUT/POST/PATCH requests to the custom resource ignore changes to
  the status stanza
  """



class CustomResourceSubresources(_messages.Message):
  r"""CustomResourceSubresources defines the status and scale subresources for
  CustomResources.

  Fields:
    scale: Scale denotes the scale subresource for CustomResources +optional
    status: Status denotes the status subresource for CustomResources
      +optional
  """

  scale = _messages.MessageField('CustomResourceSubresourceScale', 1)
  status = _messages.MessageField('CustomResourceSubresourceStatus', 2)


class CustomResourceValidation(_messages.Message):
  r"""CustomResourceValidation is a list of validation methods for
  CustomResources.

  Fields:
    openAPIV3Schema: OpenAPIV3Schema is the OpenAPI v3 schema to be validated
      against. +optional
  """

  openAPIV3Schema = _messages.MessageField('JSONSchemaProps', 1)


class ExternalDocumentation(_messages.Message):
  r"""ExternalDocumentation allows referencing an external resource for
  extended documentation.

  Fields:
    description: A string attribute.
    url: A string attribute.
  """

  description = _messages.StringField(1)
  url = _messages.StringField(2)


class JSON(_messages.Message):
  r"""JSON represents any valid JSON value. These types are supported: bool,
  int64, float64, string, []interface{}, map[string]interface{} and nil.

  Fields:
    raw: A byte attribute.
  """

  raw = _messages.BytesField(1)


class JSONSchemaProps(_messages.Message):
  r"""JSONSchemaProps is a JSON-Schema following Specification Draft 4
  (http://json-schema.org/).

  Messages:
    DefinitionsValue: A DefinitionsValue object.
    DependenciesValue: A DependenciesValue object.
    PatternPropertiesValue: A PatternPropertiesValue object.
    PropertiesValue: A PropertiesValue object.

  Fields:
    additionalItems: A JSONSchemaPropsOrBool attribute.
    additionalProperties: A JSONSchemaPropsOrBool attribute.
    allOf: A JSONSchemaProps attribute.
    anyOf: A JSONSchemaProps attribute.
    default: A JSON attribute.
    definitions: A DefinitionsValue attribute.
    dependencies: A DependenciesValue attribute.
    description: A string attribute.
    enum: A string attribute.
    example: A JSON attribute.
    exclusiveMaximum: A boolean attribute.
    exclusiveMinimum: A boolean attribute.
    externalDocs: A ExternalDocumentation attribute.
    format: A string attribute.
    id: A string attribute.
    items: A JSONSchemaPropsOrArray attribute.
    maxItems: A string attribute.
    maxLength: A string attribute.
    maxProperties: A string attribute.
    maximum: A number attribute.
    minItems: A string attribute.
    minLength: A string attribute.
    minProperties: A string attribute.
    minimum: A number attribute.
    multipleOf: A number attribute.
    not_: A JSONSchemaProps attribute.
    oneOf: A JSONSchemaProps attribute.
    pattern: A string attribute.
    patternProperties: A PatternPropertiesValue attribute.
    properties: A PropertiesValue attribute.
    ref: A string attribute.
    required: A string attribute.
    schema: A string attribute.
    title: A string attribute.
    type: A string attribute.
    uniqueItems: A boolean attribute.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DefinitionsValue(_messages.Message):
    r"""A DefinitionsValue object.

    Messages:
      AdditionalProperty: An additional property for a DefinitionsValue
        object.

    Fields:
      additionalProperties: Additional properties of type DefinitionsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DefinitionsValue object.

      Fields:
        key: Name of the additional property.
        value: A JSONSchemaProps attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('JSONSchemaProps', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DependenciesValue(_messages.Message):
    r"""A DependenciesValue object.

    Messages:
      AdditionalProperty: An additional property for a DependenciesValue
        object.

    Fields:
      additionalProperties: Additional properties of type DependenciesValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DependenciesValue object.

      Fields:
        key: Name of the additional property.
        value: A JSONSchemaPropsOrStringArray attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('JSONSchemaPropsOrStringArray', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class PatternPropertiesValue(_messages.Message):
    r"""A PatternPropertiesValue object.

    Messages:
      AdditionalProperty: An additional property for a PatternPropertiesValue
        object.

    Fields:
      additionalProperties: Additional properties of type
        PatternPropertiesValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a PatternPropertiesValue object.

      Fields:
        key: Name of the additional property.
        value: A JSONSchemaProps attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('JSONSchemaProps', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class PropertiesValue(_messages.Message):
    r"""A PropertiesValue object.

    Messages:
      AdditionalProperty: An additional property for a PropertiesValue object.

    Fields:
      additionalProperties: Additional properties of type PropertiesValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a PropertiesValue object.

      Fields:
        key: Name of the additional property.
        value: A JSONSchemaProps attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('JSONSchemaProps', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  additionalItems = _messages.MessageField('JSONSchemaPropsOrBool', 1)
  additionalProperties = _messages.MessageField('JSONSchemaPropsOrBool', 2)
  allOf = _messages.MessageField('JSONSchemaProps', 3, repeated=True)
  anyOf = _messages.MessageField('JSONSchemaProps', 4, repeated=True)
  default = _messages.MessageField('JSON', 5)
  definitions = _messages.MessageField('DefinitionsValue', 6)
  dependencies = _messages.MessageField('DependenciesValue', 7)
  description = _messages.StringField(8)
  enum = _messages.StringField(9, repeated=True)
  example = _messages.MessageField('JSON', 10)
  exclusiveMaximum = _messages.BooleanField(11)
  exclusiveMinimum = _messages.BooleanField(12)
  externalDocs = _messages.MessageField('ExternalDocumentation', 13)
  format = _messages.StringField(14)
  id = _messages.StringField(15)
  items = _messages.MessageField('JSONSchemaPropsOrArray', 16)
  maxItems = _messages.IntegerField(17)
  maxLength = _messages.IntegerField(18)
  maxProperties = _messages.IntegerField(19)
  maximum = _messages.FloatField(20)
  minItems = _messages.IntegerField(21)
  minLength = _messages.IntegerField(22)
  minProperties = _messages.IntegerField(23)
  minimum = _messages.FloatField(24)
  multipleOf = _messages.FloatField(25)
  not_ = _messages.MessageField('JSONSchemaProps', 26)
  oneOf = _messages.MessageField('JSONSchemaProps', 27, repeated=True)
  pattern = _messages.StringField(28)
  patternProperties = _messages.MessageField('PatternPropertiesValue', 29)
  properties = _messages.MessageField('PropertiesValue', 30)
  ref = _messages.StringField(31)
  required = _messages.StringField(32, repeated=True)
  schema = _messages.StringField(33)
  title = _messages.StringField(34)
  type = _messages.StringField(35)
  uniqueItems = _messages.BooleanField(36)


class JSONSchemaPropsOrArray(_messages.Message):
  r"""JSONSchemaPropsOrArray represents a value that can either be a
  JSONSchemaProps or an array of JSONSchemaProps. Mainly here for
  serialization purposes.

  Fields:
    jsonSchemas: A JSONSchemaProps attribute.
    schema: A JSONSchemaProps attribute.
  """

  jsonSchemas = _messages.MessageField('JSONSchemaProps', 1, repeated=True)
  schema = _messages.MessageField('JSONSchemaProps', 2)


class JSONSchemaPropsOrBool(_messages.Message):
  r"""JSONSchemaPropsOrBool represents JSONSchemaProps or a boolean value.
  Defaults to true for the boolean property.

  Fields:
    allows: A boolean attribute.
    schema: A JSONSchemaProps attribute.
  """

  allows = _messages.BooleanField(1)
  schema = _messages.MessageField('JSONSchemaProps', 2)


class JSONSchemaPropsOrStringArray(_messages.Message):
  r"""JSONSchemaPropsOrStringArray represents a JSONSchemaProps or a string
  array.

  Fields:
    property: A string attribute.
    schema: A JSONSchemaProps attribute.
  """

  property = _messages.StringField(1, repeated=True)
  schema = _messages.MessageField('JSONSchemaProps', 2)


class ListCustomResourceDefinitionsResponse(_messages.Message):
  r"""A ListCustomResourceDefinitionsResponse object.

  Fields:
    apiVersion: The API version for this call such as
      "k8s.apiextensions.io/v1beta1".
    items: List of CustomResourceDefinitions.
    kind: The kind of this resource, in this case
      "CustomResourceDefinitionList".
    metadata: Metadata associated with this CustomResourceDefinition list.
    unreachable: Locations that could not be reached.
  """

  apiVersion = _messages.StringField(1)
  items = _messages.MessageField('CustomResourceDefinition', 2, repeated=True)
  kind = _messages.StringField(3)
  metadata = _messages.MessageField('ListMeta', 4)
  unreachable = _messages.StringField(5, repeated=True)


class ListMeta(_messages.Message):
  r"""ListMeta describes metadata that synthetic resources must have,
  including lists and various status objects. A resource may have only one of
  {ObjectMeta, ListMeta}.

  Fields:
    continue_: continue may be set if the user set a limit on the number of
      items returned, and indicates that the server has more data available.
      The value is opaque and may be used to issue another request to the
      endpoint that served this list to retrieve the next set of available
      objects. Continuing a list may not be possible if the server
      configuration has changed or more than a few minutes have passed. The
      resourceVersion field returned when using this continue value will be
      identical to the value in the first response.
    resourceVersion: String that identifies the server's internal version of
      this object that can be used by clients to determine when objects have
      changed. Value must be treated as opaque by clients and passed
      unmodified back to the server. Populated by the system. Read-only. More
      info: https://git.k8s.io/community/contributors/devel/api-
      conventions.md#concurrency-control-and-consistency +optional
    selfLink: SelfLink is a URL representing this object. Populated by the
      system. Read-only. +optional
  """

  continue_ = _messages.StringField(1)
  resourceVersion = _messages.StringField(2)
  selfLink = _messages.StringField(3)


class ObjectMeta(_messages.Message):
  r"""k8s.io.apimachinery.pkg.apis.meta.v1.ObjectMeta is metadata that all
  persisted resources must have, which includes all objects users must create.

  Messages:
    AnnotationsValue: (Optional)  Annotations is an unstructured key value map
      stored with a resource that may be set by external tools to store and
      retrieve arbitrary metadata. They are not queryable and should be
      preserved when modifying objects. More info:
      http://kubernetes.io/docs/user-guide/annotations
    LabelsValue: (Optional)  Map of string keys and values that can be used to
      organize and categorize (scope and select) objects. May match selectors
      of replication controllers and routes. More info:
      http://kubernetes.io/docs/user-guide/labels

  Fields:
    annotations: (Optional)  Annotations is an unstructured key value map
      stored with a resource that may be set by external tools to store and
      retrieve arbitrary metadata. They are not queryable and should be
      preserved when modifying objects. More info:
      http://kubernetes.io/docs/user-guide/annotations
    clusterName: (Optional)  Cloud Run fully managed: not supported  Cloud Run
      for Anthos: supported  The name of the cluster which the object belongs
      to. This is used to distinguish resources with same name and namespace
      in different clusters. This field is not set anywhere right now and
      apiserver is going to ignore it if set in create or update request.
    creationTimestamp: (Optional)  CreationTimestamp is a timestamp
      representing the server time when this object was created. It is not
      guaranteed to be set in happens-before order across separate operations.
      Clients may not set this value. It is represented in RFC3339 form and is
      in UTC.  Populated by the system. Read-only. Null for lists. More info:
      https://git.k8s.io/community/contributors/devel/api-
      conventions.md#metadata
    deletionGracePeriodSeconds: (Optional)  Cloud Run fully managed: not
      supported  Cloud Run for Anthos: supported  Number of seconds allowed
      for this object to gracefully terminate before it will be removed from
      the system. Only set when deletionTimestamp is also set. May only be
      shortened. Read-only.
    deletionTimestamp: (Optional)  Cloud Run fully managed: not supported
      Cloud Run for Anthos: supported  DeletionTimestamp is RFC 3339 date and
      time at which this resource will be deleted. This field is set by the
      server when a graceful deletion is requested by the user, and is not
      directly settable by a client. The resource is expected to be deleted
      (no longer visible from resource lists, and not reachable by name) after
      the time in this field, once the finalizers list is empty. As long as
      the finalizers list contains items, deletion is blocked. Once the
      deletionTimestamp is set, this value may not be unset or be set further
      into the future, although it may be shortened or the resource may be
      deleted prior to this time. For example, a user may request that a pod
      is deleted in 30 seconds. The Kubelet will react by sending a graceful
      termination signal to the containers in the pod. After that 30 seconds,
      the Kubelet will send a hard termination signal (SIGKILL) to the
      container and after cleanup, remove the pod from the API. In the
      presence of network partitions, this object may still exist after this
      timestamp, until an administrator or automated process can determine the
      resource is fully terminated. If not set, graceful deletion of the
      object has not been requested.  Populated by the system when a graceful
      deletion is requested. Read-only. More info:
      https://git.k8s.io/community/contributors/devel/api-
      conventions.md#metadata
    finalizers: (Optional)  Cloud Run fully managed: not supported  Cloud Run
      for Anthos: supported  Must be empty before the object is deleted from
      the registry. Each entry is an identifier for the responsible component
      that will remove the entry from the list. If the deletionTimestamp of
      the object is non-nil, entries in this list can only be removed.
      +patchStrategy=merge
    generateName: (Optional)  Cloud Run fully managed: not supported  Cloud
      Run for Anthos: supported  GenerateName is an optional prefix, used by
      the server, to generate a unique name ONLY IF the Name field has not
      been provided. If this field is used, the name returned to the client
      will be different than the name passed. This value will also be combined
      with a unique suffix. The provided value has the same validation rules
      as the Name field, and may be truncated by the length of the suffix
      required to make the value unique on the server.  If this field is
      specified and the generated name exists, the server will NOT return a
      409 - instead, it will either return 201 Created or 500 with Reason
      ServerTimeout indicating a unique name could not be found in the time
      allotted, and the client should retry (optionally after the time
      indicated in the Retry-After header).  Applied only if Name is not
      specified. More info:
      https://git.k8s.io/community/contributors/devel/api-
      conventions.md#idempotency  string generateName = 2;
    generation: (Optional)  A sequence number representing a specific
      generation of the desired state. Populated by the system. Read-only.
    labels: (Optional)  Map of string keys and values that can be used to
      organize and categorize (scope and select) objects. May match selectors
      of replication controllers and routes. More info:
      http://kubernetes.io/docs/user-guide/labels
    name: Name must be unique within a namespace, within a Cloud Run region.
      Is required when creating resources, although some resources may allow a
      client to request the generation of an appropriate name automatically.
      Name is primarily intended for creation idempotence and configuration
      definition. Cannot be updated. More info:
      http://kubernetes.io/docs/user-guide/identifiers#names +optional
    namespace: Namespace defines the space within each name must be unique,
      within a Cloud Run region. In Cloud Run the namespace must be equal to
      either the project ID or project number.
    ownerReferences: (Optional)  Cloud Run fully managed: not supported  Cloud
      Run for Anthos: supported  List of objects that own this object. If ALL
      objects in the list have been deleted, this object will be garbage
      collected.
    resourceVersion: (Optional)  An opaque value that represents the internal
      version of this object that can be used by clients to determine when
      objects have changed. May be used for optimistic concurrency, change
      detection, and the watch operation on a resource or set of resources.
      Clients must treat these values as opaque and passed unmodified back to
      the server. They may only be valid for a particular resource or set of
      resources.  Populated by the system. Read-only. Value must be treated as
      opaque by clients and . More info:
      https://git.k8s.io/community/contributors/devel/api-
      conventions.md#concurrency-control-and-consistency
    selfLink: (Optional)  SelfLink is a URL representing this object.
      Populated by the system. Read-only.  string selfLink = 4;
    uid: (Optional)  UID is the unique in time and space value for this
      object. It is typically generated by the server on successful creation
      of a resource and is not allowed to change on PUT operations.  Populated
      by the system. Read-only. More info: http://kubernetes.io/docs/user-
      guide/identifiers#uids
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class AnnotationsValue(_messages.Message):
    r"""(Optional)  Annotations is an unstructured key value map stored with a
    resource that may be set by external tools to store and retrieve arbitrary
    metadata. They are not queryable and should be preserved when modifying
    objects. More info: http://kubernetes.io/docs/user-guide/annotations

    Messages:
      AdditionalProperty: An additional property for a AnnotationsValue
        object.

    Fields:
      additionalProperties: Additional properties of type AnnotationsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a AnnotationsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""(Optional)  Map of string keys and values that can be used to organize
    and categorize (scope and select) objects. May match selectors of
    replication controllers and routes. More info:
    http://kubernetes.io/docs/user-guide/labels

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

  annotations = _messages.MessageField('AnnotationsValue', 1)
  clusterName = _messages.StringField(2)
  creationTimestamp = _messages.StringField(3)
  deletionGracePeriodSeconds = _messages.IntegerField(4, variant=_messages.Variant.INT32)
  deletionTimestamp = _messages.StringField(5)
  finalizers = _messages.StringField(6, repeated=True)
  generateName = _messages.StringField(7)
  generation = _messages.IntegerField(8, variant=_messages.Variant.INT32)
  labels = _messages.MessageField('LabelsValue', 9)
  name = _messages.StringField(10)
  namespace = _messages.StringField(11)
  ownerReferences = _messages.MessageField('OwnerReference', 12, repeated=True)
  resourceVersion = _messages.StringField(13)
  selfLink = _messages.StringField(14)
  uid = _messages.StringField(15)


class OwnerReference(_messages.Message):
  r"""OwnerReference contains enough information to let you identify an owning
  object. Currently, an owning object must be in the same namespace, so there
  is no namespace field.

  Fields:
    apiVersion: API version of the referent.
    blockOwnerDeletion: If true, AND if the owner has the "foregroundDeletion"
      finalizer, then the owner cannot be deleted from the key-value store
      until this reference is removed. Defaults to false. To set this field, a
      user needs "delete" permission of the owner, otherwise 422
      (Unprocessable Entity) will be returned. +optional
    controller: If true, this reference points to the managing controller.
      +optional
    kind: Kind of the referent. More info:
      https://git.k8s.io/community/contributors/devel/api-
      conventions.md#types-kinds
    name: Name of the referent. More info: http://kubernetes.io/docs/user-
      guide/identifiers#names
    uid: UID of the referent. More info: http://kubernetes.io/docs/user-
      guide/identifiers#uids
  """

  apiVersion = _messages.StringField(1)
  blockOwnerDeletion = _messages.BooleanField(2)
  controller = _messages.BooleanField(3)
  kind = _messages.StringField(4)
  name = _messages.StringField(5)
  uid = _messages.StringField(6)


class RunCustomresourcedefinitionsListRequest(_messages.Message):
  r"""A RunCustomresourcedefinitionsListRequest object.

  Fields:
    continue_: Optional encoded string to continue paging.
    fieldSelector: Allows to filter resources based on a specific value for a
      field name. Send this in a query string format. i.e.
      'metadata.name%3Dlorem'. Not currently used by Cloud Run.
    includeUninitialized: Not currently used by Cloud Run.
    labelSelector: Allows to filter resources based on a label. Supported
      operations are =, !=, exists, in, and notIn.
    limit: A integer attribute.
    parent: The project ID or project number from which the storages should be
      listed.
    resourceVersion: The baseline resource version from which the list or
      watch operation should start. Not currently used by Cloud Run.
    watch: Flag that indicates that the client expects to watch this resource
      as well. Not currently used by Cloud Run.
  """

  continue_ = _messages.StringField(1)
  fieldSelector = _messages.StringField(2)
  includeUninitialized = _messages.BooleanField(3)
  labelSelector = _messages.StringField(4)
  limit = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  parent = _messages.StringField(6)
  resourceVersion = _messages.StringField(7)
  watch = _messages.BooleanField(8)


class RunNamespacesCustomresourcedefinitionsGetRequest(_messages.Message):
  r"""A RunNamespacesCustomresourcedefinitionsGetRequest object.

  Fields:
    name: The name of the CustomResourceDefinition being retrieved. If needed,
      replace {namespace_id} with the project ID.
  """

  name = _messages.StringField(1, required=True)


class RunProjectsLocationsCustomresourcedefinitionsGetRequest(_messages.Message):
  r"""A RunProjectsLocationsCustomresourcedefinitionsGetRequest object.

  Fields:
    name: The name of the CustomResourceDefinition being retrieved. If needed,
      replace {namespace_id} with the project ID.
  """

  name = _messages.StringField(1, required=True)


class RunProjectsLocationsCustomresourcedefinitionsListRequest(_messages.Message):
  r"""A RunProjectsLocationsCustomresourcedefinitionsListRequest object.

  Fields:
    continue_: Optional encoded string to continue paging.
    fieldSelector: Allows to filter resources based on a specific value for a
      field name. Send this in a query string format. i.e.
      'metadata.name%3Dlorem'. Not currently used by Cloud Run.
    includeUninitialized: Not currently used by Cloud Run.
    labelSelector: Allows to filter resources based on a label. Supported
      operations are =, !=, exists, in, and notIn.
    limit: A integer attribute.
    parent: The project ID or project number from which the storages should be
      listed.
    resourceVersion: The baseline resource version from which the list or
      watch operation should start. Not currently used by Cloud Run.
    watch: Flag that indicates that the client expects to watch this resource
      as well. Not currently used by Cloud Run.
  """

  continue_ = _messages.StringField(1)
  fieldSelector = _messages.StringField(2)
  includeUninitialized = _messages.BooleanField(3)
  labelSelector = _messages.StringField(4)
  limit = _messages.IntegerField(5, variant=_messages.Variant.INT32)
  parent = _messages.StringField(6, required=True)
  resourceVersion = _messages.StringField(7)
  watch = _messages.BooleanField(8)


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
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


encoding.AddCustomJsonFieldMapping(
    JSONSchemaProps, 'not_', 'not')
encoding.AddCustomJsonFieldMapping(
    ListMeta, 'continue_', 'continue')
encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
