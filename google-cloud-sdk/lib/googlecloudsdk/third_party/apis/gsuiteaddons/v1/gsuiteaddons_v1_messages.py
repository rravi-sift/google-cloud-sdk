"""Generated message classes for gsuiteaddons version v1.

"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'gsuiteaddons'


class GoogleAppsScriptTypeAddOnWidgetSet(_messages.Message):
  r"""The widget subset used by an add-on.

  Enums:
    UsedWidgetsValueListEntryValuesEnum:

  Fields:
    usedWidgets: The list of widgets used in an add-on.
  """

  class UsedWidgetsValueListEntryValuesEnum(_messages.Enum):
    r"""UsedWidgetsValueListEntryValuesEnum enum type.

    Values:
      WIDGET_TYPE_UNSPECIFIED: The default widget set.
      DATE_PICKER: The date picker.
      STYLED_BUTTONS: Styled buttons include filled buttons and disabled
        buttons.
      PERSISTENT_FORMS: Persistent forms allow persisting form values during
        actions.
      FIXED_FOOTER: Fixed footer in card.
      UPDATE_SUBJECT_AND_RECIPIENTS: Update the subject and recipients of a
        draft.
    """
    WIDGET_TYPE_UNSPECIFIED = 0
    DATE_PICKER = 1
    STYLED_BUTTONS = 2
    PERSISTENT_FORMS = 3
    FIXED_FOOTER = 4
    UPDATE_SUBJECT_AND_RECIPIENTS = 5

  usedWidgets = _messages.EnumField('UsedWidgetsValueListEntryValuesEnum', 1, repeated=True)


class GoogleAppsScriptTypeCalendarCalendarAddOnManifest(_messages.Message):
  r"""Calendar add-on manifest.

  Enums:
    CurrentEventAccessValueValuesEnum: Define the level of data access when an
      event addon is triggered.

  Fields:
    conferenceSolution: Defines conference solutions provided by this add-on.
    createSettingsUrlFunction: A function in the add-on that creates a URL to
      the add-on's settings page.
    currentEventAccess: Define the level of data access when an event addon is
      triggered.
    eventOpenTrigger: Function in the add-on to trigger when an event is
      opened (viewed/edited).
    eventUpdateTrigger: Function in the add-on to trigger when the open event
      is updated.
    homepageTrigger: Defines an Apps Script function that will be executed
      contexts that don't match a declared contextual trigger. Any cards
      generated by this function will always be available to the user, but may
      be eclipsed by contextual content when this add-on declares more
      targeted triggers. If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
  """

  class CurrentEventAccessValueValuesEnum(_messages.Enum):
    r"""Define the level of data access when an event addon is triggered.

    Values:
      UNSPECIFIED: Default value when nothing is set for EventAccess.
      METADATA: METADATA gives event triggers the permission to access the
        metadata of events such as event id and calendar id.
      READ: READ gives event triggers access to all provided event fields
        including the metadata, attendees, and conference data.
      WRITE: WRITE gives event triggers access to the metadata of events and
        the ability to perform all actions, including adding attendees and
        setting conference data.
      READ_WRITE: READ_WRITE gives event triggers access to all provided event
        fields including the metadata, attendees, and conference data and the
        ability to perform all actions.
    """
    UNSPECIFIED = 0
    METADATA = 1
    READ = 2
    WRITE = 3
    READ_WRITE = 4

  conferenceSolution = _messages.MessageField('GoogleAppsScriptTypeCalendarConferenceSolution', 1, repeated=True)
  createSettingsUrlFunction = _messages.StringField(2)
  currentEventAccess = _messages.EnumField('CurrentEventAccessValueValuesEnum', 3)
  eventOpenTrigger = _messages.MessageField('GoogleAppsScriptTypeCalendarCalendarExtensionPoint', 4)
  eventUpdateTrigger = _messages.MessageField('GoogleAppsScriptTypeCalendarCalendarExtensionPoint', 5)
  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 6)


class GoogleAppsScriptTypeCalendarCalendarExtensionPoint(_messages.Message):
  r"""Common format for declaring a calendar add-on's triggers. Next ID: 2

  Fields:
    runFunction: Required. The Apps Script function to execute when this
      extension point is activated.
  """

  runFunction = _messages.StringField(1)


class GoogleAppsScriptTypeCalendarConferenceSolution(_messages.Message):
  r"""Defines conference related values.

  Fields:
    id: Required. IDs should be unique across ConferenceSolutions within one
      add-on, but this is not strictly enforced. It is up to the add-on
      developer to assign them uniquely, otherwise the wrong
      ConferenceSolution may be used when the add-on is triggered. While the
      developer may change the display name of an add-on, the ID should not be
      changed.
    logoUrl: Required. The URL for the logo image of the ConferenceSolution.
    name: Required. The display name of the ConferenceSolution.
    onCreateFunction: Required. The method to call when ConferenceData should
      be created.
  """

  id = _messages.StringField(1)
  logoUrl = _messages.StringField(2)
  name = _messages.StringField(3)
  onCreateFunction = _messages.StringField(4)


class GoogleAppsScriptTypeCommonAddOnManifest(_messages.Message):
  r"""Add-on configuration that is shared across all add-on host applications.

  Fields:
    addOnWidgetSet: The widgets used in a gmail add-on. If this field is not
      specified, it indicates that default set is used.
    homepageTrigger: Defines an Apps Script function that will be executed in
      any context, in any host. Any cards generated by this function will
      always be available to the user, but may be eclipsed by contextual
      content when this add-on declares more targeted triggers.
    layoutProperties: Common layout properties for the add-on cards.
    logoUrl: Required. The URL for the logo image shown in the add-on toolbar.
    name: Required. The display name of the add-on.
    openLinkUrlPrefixes: An OpenLink action can only use a URL with an HTTPS,
      MAILTO or TEL scheme. For HTTPS links, the URL must also
      [match](/gmail/add-ons/concepts/manifests#whitelisting_urls) one of the
      prefixes specified in this whitelist. If the prefix omits the scheme,
      HTTPS is assumed. Notice that HTTP links are automatically rewritten to
      HTTPS links.
    universalActions: Defines a list of extension points in the universal
      action menu which serves as a setting menu for the add-on. The extension
      point can be link URL to open or an Apps Script function to execute as a
      form submission.
    useLocaleFromApp: Whether to pass locale information from host app.
  """

  addOnWidgetSet = _messages.MessageField('GoogleAppsScriptTypeAddOnWidgetSet', 1)
  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 2)
  layoutProperties = _messages.MessageField('GoogleAppsScriptTypeLayoutProperties', 3)
  logoUrl = _messages.StringField(4)
  name = _messages.StringField(5)
  openLinkUrlPrefixes = _messages.MessageField('extra_types.JsonValue', 6, repeated=True)
  universalActions = _messages.MessageField('GoogleAppsScriptTypeUniversalActionExtensionPoint', 7, repeated=True)
  useLocaleFromApp = _messages.BooleanField(8)


class GoogleAppsScriptTypeDocsDocsAddOnManifest(_messages.Message):
  r"""Docs add-on manifest.

  Fields:
    homepageTrigger: If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
    onFileScopeGrantedTrigger: Function in the add-on to trigger when file
      scope authorization is granted for this document/user pair.
  """

  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 1)
  onFileScopeGrantedTrigger = _messages.MessageField('GoogleAppsScriptTypeDocsDocsExtensionPoint', 2)


class GoogleAppsScriptTypeDocsDocsExtensionPoint(_messages.Message):
  r"""Common format for declaring a Docs add-on's triggers.

  Fields:
    runFunction: Required. The Apps Script function to execute when this
      extension point is activated.
  """

  runFunction = _messages.StringField(1)


class GoogleAppsScriptTypeDrawingsDrawingsAddOnManifest(_messages.Message):
  r"""Drawings add-on manifest.

  Fields:
    homepageTrigger: If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
  """

  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 1)


class GoogleAppsScriptTypeDriveDriveAddOnManifest(_messages.Message):
  r"""Drive add-on manifest.

  Fields:
    homepageTrigger: If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
    onItemsSelectedTrigger: Corresponds to behvior that should execute when
      items are selected in relevant Drive view (e.g. the My Drive Doclist).
  """

  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 1)
  onItemsSelectedTrigger = _messages.MessageField('GoogleAppsScriptTypeDriveDriveExtensionPoint', 2)


class GoogleAppsScriptTypeDriveDriveExtensionPoint(_messages.Message):
  r"""A generic extension point with common features, e.g. something that
  simply needs a corresponding run function to work.

  Fields:
    runFunction: Required. The Apps Script function to execute when this
      extension point is activated.
  """

  runFunction = _messages.StringField(1)


class GoogleAppsScriptTypeFormsFormsAddOnManifest(_messages.Message):
  r"""Forms add-on manifest."""


class GoogleAppsScriptTypeGmailComposeTrigger(_messages.Message):
  r"""A trigger that activates when user is composing an email.

  Enums:
    DraftAccessValueValuesEnum: Define the level of data access when a compose
      time addon is triggered.

  Fields:
    actions: Defines the set of [actions]() for compose time add-on. These are
      actions that user can trigger on a compose time addon.
    draftAccess: Define the level of data access when a compose time addon is
      triggered.
    selectActions: A GoogleAppsScriptTypeGmailComposeTriggerSelectAction
      attribute.
  """

  class DraftAccessValueValuesEnum(_messages.Enum):
    r"""Define the level of data access when a compose time addon is
    triggered.

    Values:
      UNSPECIFIED: Default value when nothing is set for DraftAccess.
      NONE: NONE means compose trigger won't be able to access any data of the
        draft when a compose addon is triggered.
      METADATA: METADATA gives compose trigger the permission to access the
        metadata of the draft when a compose addon is triggered. This includes
        the audience list (To/cc list) of a draft message.
    """
    UNSPECIFIED = 0
    NONE = 1
    METADATA = 2

  actions = _messages.MessageField('GoogleAppsScriptTypeMenuItemExtensionPoint', 1, repeated=True)
  draftAccess = _messages.EnumField('DraftAccessValueValuesEnum', 2)
  selectActions = _messages.MessageField('GoogleAppsScriptTypeGmailComposeTriggerSelectAction', 3, repeated=True)


class GoogleAppsScriptTypeGmailComposeTriggerSelectAction(_messages.Message):
  r"""A GoogleAppsScriptTypeGmailComposeTriggerSelectAction object.

  Fields:
    runFunction: A string attribute.
    text: A string attribute.
  """

  runFunction = _messages.StringField(1)
  text = _messages.StringField(2)


class GoogleAppsScriptTypeGmailContextualTrigger(_messages.Message):
  r"""Defines a trigger that fires when the open email meets a specific
  criteria. When the trigger fires, it executes a specific Apps Script
  function, usually in order to create new cards and update the UI. Every add-
  on must define either a contextual trigger and/or a set of universal
  actions.

  Fields:
    onTriggerFunction: Required. The name of the function to call when a
      message matches the trigger.
    unconditional: UnconditionalTriggers are executed when any mail message is
      opened.
  """

  onTriggerFunction = _messages.StringField(1)
  unconditional = _messages.MessageField('GoogleAppsScriptTypeGmailUnconditionalTrigger', 2)


class GoogleAppsScriptTypeGmailGmailAddOnManifest(_messages.Message):
  r"""Properties customizing the appearance and execution of a Gmail add-on.

  Fields:
    authorizationCheckFunction: The name of an Apps Script function that
      verifies that the add-on has all the required third-party
      authorizations, by probing the third-party APIs. If the probe fails, the
      function should throw an exception to initiate the authorization flow.
      This function is called before each invocation of the add-on, in order
      to ensure a smooth user experience.
    composeTrigger: Defines the [compose time trigger]() for a compose time
      add-on. This is the trigger that causes an add-on to take action when
      the user is composing an email. All compose time addons are forced to
      have the gmail.addons.current.action .compose scope even though it might
      not edit the draft. If there is compelling use case which doest not need
      to edit the draft, we can consider adding a field allow developers to
      specify whether they will modify the draft.
    contextualTriggers: Defines the set of conditions that trigger the add-on.
    homepageTrigger: Defines an Apps Script function that will be executed
      contexts that don't match a declared contextual trigger. Any cards
      generated by this function will always be available to the user, but may
      be eclipsed by contextual content when this add-on declares more
      targeted triggers. If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
    logoUrl: Required. The URL for the logo image shown in the add-on toolbar.
    name: Required. The display name of the add-on.
    openLinkUrlPrefixes: An OpenLink action can only use a URL with an HTTPS,
      MAILTO or TEL scheme. For HTTPS links, the URL must also
      [match](/gmail/add-ons/concepts/manifests#whitelisting_urls) one of the
      prefixes specified in this whitelist. If the prefix omits the scheme,
      HTTPS is assumed. Notice that HTTP links are automatically rewritten to
      HTTPS links.
    primaryColor: The primary color of the add-on. It sets the color of
      toolbar. If no primary color is set explicitly, the default value
      provided by the framework is used.
    secondaryColor: The secondary color of the add-on. It sets the color of
      buttons. If primary color is set but no secondary color is set, the
      secondary color is the same as the primary color. If neither primary
      color nor secondary color is set, the default value provided by the
      framework is used.
    universalActions: Defines set of [universal actions](/gmail/add-ons/how-
      tos/universal-actions) for the add-on. The user triggers universal
      actions from the add-on toolbar menu.
  """

  authorizationCheckFunction = _messages.StringField(1)
  composeTrigger = _messages.MessageField('GoogleAppsScriptTypeGmailComposeTrigger', 2)
  contextualTriggers = _messages.MessageField('GoogleAppsScriptTypeGmailContextualTrigger', 3, repeated=True)
  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 4)
  logoUrl = _messages.StringField(5)
  name = _messages.StringField(6)
  openLinkUrlPrefixes = _messages.MessageField('extra_types.JsonValue', 7, repeated=True)
  primaryColor = _messages.StringField(8)
  secondaryColor = _messages.StringField(9)
  universalActions = _messages.MessageField('GoogleAppsScriptTypeGmailUniversalAction', 10, repeated=True)


class GoogleAppsScriptTypeGmailUnconditionalTrigger(_messages.Message):
  r"""A trigger that fires when any email message is opened."""


class GoogleAppsScriptTypeGmailUniversalAction(_messages.Message):
  r"""An action that is always available in the add-on toolbar menu regardless
  of message context.

  Fields:
    openLink: A link that is opened by Gmail when the user triggers the
      action.
    runFunction: An Apps Script function that is called when the user triggers
      the action. See the [universal actions guide](/gmail/add-ons/how-
      tos/universal-actions) for details.
    text: Required. User-visible text describing the action, for example, "Add
      a new contact."
  """

  openLink = _messages.StringField(1)
  runFunction = _messages.StringField(2)
  text = _messages.StringField(3)


class GoogleAppsScriptTypeHomepageExtensionPoint(_messages.Message):
  r"""Common format for declaring an add-on's home-page view.

  Fields:
    enabled: Optional. If set to `false`, disable the home-page view in this
      context. Defaults to `true` if unset. If an add-ons custom home-page
      view is disabled, an autogenerated overview card will be provided for
      users instead.
    runFunction: Required. The Apps Script function to execute when this
      extension point is activated.
  """

  enabled = _messages.BooleanField(1)
  runFunction = _messages.StringField(2)


class GoogleAppsScriptTypeHttpOptions(_messages.Message):
  r"""Options for sending requests to add-on HTTP endpoints

  Enums:
    AuthorizationHeaderValueValuesEnum: Configuration for the token sent in
      the HTTP Authorization header

  Fields:
    authorizationHeader: Configuration for the token sent in the HTTP
      Authorization header
  """

  class AuthorizationHeaderValueValuesEnum(_messages.Enum):
    r"""Configuration for the token sent in the HTTP Authorization header

    Values:
      UNKNOWN_AUTHORIZATION_HEADER: Send an ID token for the project-specific
        G Suite Add-ons system service account (default)
      SYSTEM_ID_TOKEN: Send an ID token for the project-specific G Suite Add-
        ons system service account (default)
      USER_ID_TOKEN: Send an ID token for the end user
      NONE: Do not send an Authentication header
    """
    UNKNOWN_AUTHORIZATION_HEADER = 0
    SYSTEM_ID_TOKEN = 1
    USER_ID_TOKEN = 2
    NONE = 3

  authorizationHeader = _messages.EnumField('AuthorizationHeaderValueValuesEnum', 1)


class GoogleAppsScriptTypeLayoutProperties(_messages.Message):
  r"""Card layout properties shared across all add-on host applications.

  Fields:
    primaryColor: The primary color of the add-on. It sets the color of
      toolbar. If no primary color is set explicitly, the default value
      provided by the framework is used.
    secondaryColor: The secondary color of the add-on. It sets the color of
      buttons. If primary color is set but no secondary color is set, the
      secondary color is the same as the primary color. If neither primary
      color nor secondary color is set, the default value provided by the
      framework is used.
  """

  primaryColor = _messages.StringField(1)
  secondaryColor = _messages.StringField(2)


class GoogleAppsScriptTypeMenuItemExtensionPoint(_messages.Message):
  r"""Common format for declaring a menu item, or button, that appears within
  a host app.

  Fields:
    label: Required. User-visible text describing the action taken by
      activating this extension point. For example, "Insert invoice".
    logoUrl: The URL for the logo image shown in the add-on toolbar. If not
      set, defaults to the add-on's primary logo URL.
    runFunction: Required. The Apps Script function to execute when this
      extension point is activated.
  """

  label = _messages.StringField(1)
  logoUrl = _messages.StringField(2)
  runFunction = _messages.StringField(3)


class GoogleAppsScriptTypeSheetsSheetsActionDefinition(_messages.Message):
  r"""Defines a script action within Sheets.

  Fields:
    defaultShortcut: Optional. The default shortcut in Sheets to execute the
      macro (e.g., "Ctrl+Alt+Shift+0")
    functionName: Required. The name of the function which performs the macro.
    menuName: Required. The name of the macro, used for display purposes.
  """

  defaultShortcut = _messages.StringField(1)
  functionName = _messages.StringField(2)
  menuName = _messages.StringField(3)


class GoogleAppsScriptTypeSheetsSheetsAddOnManifest(_messages.Message):
  r"""Sheets add-on manifest.

  Fields:
    homepageTrigger: If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
    macros: Defines Sheets actions (macros) contained within the project.
    onFileScopeGrantedTrigger: Function in the add-on to trigger when file
      scope authorization is granted for this document/user pair.
    onSelectionTrigger: Function in the add-on to trigger when a selection in
      the Sheets client occurs.
  """

  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 1)
  macros = _messages.MessageField('GoogleAppsScriptTypeSheetsSheetsActionDefinition', 2, repeated=True)
  onFileScopeGrantedTrigger = _messages.MessageField('GoogleAppsScriptTypeSheetsSheetsExtensionPoint', 3)
  onSelectionTrigger = _messages.MessageField('GoogleAppsScriptTypeSheetsSheetsExtensionPoint', 4)


class GoogleAppsScriptTypeSheetsSheetsExtensionPoint(_messages.Message):
  r"""Common format for declaring a Sheets add-on's triggers.

  Fields:
    runFunction: Required. The Apps Script function to execute when this
      extension point is activated.
  """

  runFunction = _messages.StringField(1)


class GoogleAppsScriptTypeSlidesSlidesAddOnManifest(_messages.Message):
  r"""Slides add-on manifest.

  Fields:
    homepageTrigger: If present, this overrides the configuration from
      `addOns.common.homepageTrigger`.
    onFileScopeGrantedTrigger: Function in the add-on to trigger when file
      scope authorization is granted for this document/user pair.
  """

  homepageTrigger = _messages.MessageField('GoogleAppsScriptTypeHomepageExtensionPoint', 1)
  onFileScopeGrantedTrigger = _messages.MessageField('GoogleAppsScriptTypeSlidesSlidesExtensionPoint', 2)


class GoogleAppsScriptTypeSlidesSlidesExtensionPoint(_messages.Message):
  r"""Common format for declaring a Slides add-on's triggers.

  Fields:
    runFunction: Required. The Apps Script function to execute when this
      extension point is activated.
  """

  runFunction = _messages.StringField(1)


class GoogleAppsScriptTypeUniversalActionExtensionPoint(_messages.Message):
  r"""Format for declaring a universal action menu item extension point.

  Fields:
    label: Required. User-visible text describing the action taken by
      activating this extension point, for example, "Add a new contact".
    openLink: URL to be opened by the UniversalAction.
    runFunction: Method to be run by the UniversalAction.
  """

  label = _messages.StringField(1)
  openLink = _messages.StringField(2)
  runFunction = _messages.StringField(3)


class GoogleCloudGsuiteaddonsV1AddOns(_messages.Message):
  r"""A G Suite Add-on configuration.

  Fields:
    calendar: Calendar add-on configuration.
    common: Configuration that is common across all G Suite add-ons.
    docs: Docs add-on configuration.
    drawings: Slides add-on configuration.
    drive: Drive add-on configuration.
    forms: Forms add-on configuration.
    gmail: Gmail add-on configuration.
    httpOptions: Options for sending request to add-on HTTP endpoints
    sheets: Sheets add-on configuration.
    slides: Slides add-on configuration.
  """

  calendar = _messages.MessageField('GoogleAppsScriptTypeCalendarCalendarAddOnManifest', 1)
  common = _messages.MessageField('GoogleAppsScriptTypeCommonAddOnManifest', 2)
  docs = _messages.MessageField('GoogleAppsScriptTypeDocsDocsAddOnManifest', 3)
  drawings = _messages.MessageField('GoogleAppsScriptTypeDrawingsDrawingsAddOnManifest', 4)
  drive = _messages.MessageField('GoogleAppsScriptTypeDriveDriveAddOnManifest', 5)
  forms = _messages.MessageField('GoogleAppsScriptTypeFormsFormsAddOnManifest', 6)
  gmail = _messages.MessageField('GoogleAppsScriptTypeGmailGmailAddOnManifest', 7)
  httpOptions = _messages.MessageField('GoogleAppsScriptTypeHttpOptions', 8)
  sheets = _messages.MessageField('GoogleAppsScriptTypeSheetsSheetsAddOnManifest', 9)
  slides = _messages.MessageField('GoogleAppsScriptTypeSlidesSlidesAddOnManifest', 10)


class GoogleCloudGsuiteaddonsV1Authorization(_messages.Message):
  r"""The authorization information used when invoking deployment endpoints.

  Fields:
    name: The full name of this resource. Example:
      `projects/my_project/authorization`
    oauthClientId: The OAuth client ID used to obtain OAuth access tokens for
      a user on the add-on's behalf. This is the client ID you will need to
      get whitelisted in order to publish an add-on.
    serviceAccountEmail: The email address of the service account used to
      authenticate requests to add-on callback endpoints.
  """

  name = _messages.StringField(1)
  oauthClientId = _messages.StringField(2)
  serviceAccountEmail = _messages.StringField(3)


class GoogleCloudGsuiteaddonsV1Deployment(_messages.Message):
  r"""A G Suite Add-on Deployment

  Fields:
    addOns: The G Suite Add-on configuration.
    displayName: A free-form display name for the Deployment.
    etag: This checksum is computed by the server based on the value of other
      fields, and may be sent on update and delete requests to ensure the
      client has an up-to-date value before proceeding.
    name: The deployment resource name. This field is read-only. Example:
      projects/my_project/deployments/my_deployment.
    oauthScopes: The list of Google OAuth scopes for which to request consent
      from the end user before executing an add-on endpoint.
  """

  addOns = _messages.MessageField('GoogleCloudGsuiteaddonsV1AddOns', 1)
  displayName = _messages.StringField(2)
  etag = _messages.StringField(3)
  name = _messages.StringField(4)
  oauthScopes = _messages.StringField(5, repeated=True)


class GoogleCloudGsuiteaddonsV1InstallDeploymentRequest(_messages.Message):
  r"""Request message to install a developer mode deployment."""


class GoogleCloudGsuiteaddonsV1InstallStatus(_messages.Message):
  r"""Developer mode install status of a deployment

  Fields:
    installed: True if the deployment is installed for the user
    name: The full resource name of the deployment install status. Example:
      `projects/my_project/deployments/my_deployment/installStatus`.
  """

  installed = _messages.BooleanField(1)
  name = _messages.StringField(2)


class GoogleCloudGsuiteaddonsV1ListDeploymentsResponse(_messages.Message):
  r"""Response message to list deployments.

  Fields:
    deployments: The list of deployments for the given project.
    nextPageToken: A token, which can be sent as `page_token` to retrieve the
      next page. If this field is omitted, there are no subsequent pages.
  """

  deployments = _messages.MessageField('GoogleCloudGsuiteaddonsV1Deployment', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class GoogleCloudGsuiteaddonsV1UninstallDeploymentRequest(_messages.Message):
  r"""Request message to uninstall a developer mode deployment."""


class GoogleProtobufEmpty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance: service Foo { rpc
  Bar(google.protobuf.Empty) returns (google.protobuf.Empty); } The JSON
  representation for `Empty` is empty JSON object `{}`.
  """



class GsuiteaddonsProjectsDeploymentsCreateRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsCreateRequest object.

  Fields:
    deploymentId: Required. The id to use for this deployment. The full name
      of the created resource will be `projects//deployments/`.
    googleCloudGsuiteaddonsV1Deployment: A GoogleCloudGsuiteaddonsV1Deployment
      resource to be passed as the request body.
    parent: Required. Name of the project in which to create the deployment.
      Example: `projects/my_project`.
  """

  deploymentId = _messages.StringField(1)
  googleCloudGsuiteaddonsV1Deployment = _messages.MessageField('GoogleCloudGsuiteaddonsV1Deployment', 2)
  parent = _messages.StringField(3, required=True)


class GsuiteaddonsProjectsDeploymentsDeleteRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsDeleteRequest object.

  Fields:
    etag: The etag of the deployment to delete. If this is provided, it must
      match the server's etag.
    name: Required. The full resource name of the deployment to delete.
      Example: `projects/my_project/deployments/my_deployment`.
  """

  etag = _messages.StringField(1)
  name = _messages.StringField(2, required=True)


class GsuiteaddonsProjectsDeploymentsGetInstallStatusRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsGetInstallStatusRequest object.

  Fields:
    name: Required. The full resource name of the deployment. Example:
      `projects/my_project/deployments/my_deployment/installStatus`.
  """

  name = _messages.StringField(1, required=True)


class GsuiteaddonsProjectsDeploymentsGetRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsGetRequest object.

  Fields:
    name: Required. The full resource name of the deployment to get. Example:
      `projects/my_project/deployments/my_deployment`.
  """

  name = _messages.StringField(1, required=True)


class GsuiteaddonsProjectsDeploymentsInstallRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsInstallRequest object.

  Fields:
    googleCloudGsuiteaddonsV1InstallDeploymentRequest: A
      GoogleCloudGsuiteaddonsV1InstallDeploymentRequest resource to be passed
      as the request body.
    name: Required. The full resource name of the deployment to install.
      Example: `projects/my_project/deployments/my_deployment`.
  """

  googleCloudGsuiteaddonsV1InstallDeploymentRequest = _messages.MessageField('GoogleCloudGsuiteaddonsV1InstallDeploymentRequest', 1)
  name = _messages.StringField(2, required=True)


class GsuiteaddonsProjectsDeploymentsListRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsListRequest object.

  Fields:
    pageSize: The maximum number of Deployments to return. The service may
      return fewer than this value. If unspecified, at most 1000 Deployments
      will be returned. The maximum value is 1000; values above 1000 will be
      coerced to 1000.
    pageToken: A page token, received from a previous `ListDeployments` call.
      Provide this to retrieve the subsequent page. When paginating, all other
      parameters provided to `ListDeployments` must match the call that
      provided the page token.
    parent: Required. Name of the project in which to create the deployment.
      Example: `projects/my_project`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class GsuiteaddonsProjectsDeploymentsUninstallRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsDeploymentsUninstallRequest object.

  Fields:
    googleCloudGsuiteaddonsV1UninstallDeploymentRequest: A
      GoogleCloudGsuiteaddonsV1UninstallDeploymentRequest resource to be
      passed as the request body.
    name: Required. The full resource name of the deployment to install.
      Example: `projects/my_project/deployments/my_deployment`.
  """

  googleCloudGsuiteaddonsV1UninstallDeploymentRequest = _messages.MessageField('GoogleCloudGsuiteaddonsV1UninstallDeploymentRequest', 1)
  name = _messages.StringField(2, required=True)


class GsuiteaddonsProjectsGetAuthorizationRequest(_messages.Message):
  r"""A GsuiteaddonsProjectsGetAuthorizationRequest object.

  Fields:
    name: Required. Name of the project for which to get the G Suite Add-ons
      authorization information. Example: `projects/my_project/authorization`.
  """

  name = _messages.StringField(1, required=True)


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
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
