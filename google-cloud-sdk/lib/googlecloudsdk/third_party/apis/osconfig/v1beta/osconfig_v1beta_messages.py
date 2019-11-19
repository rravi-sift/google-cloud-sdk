"""Generated message classes for osconfig version v1beta.

OS management tools that can be used for patch management, patch compliance,
and configuration management on VM instances.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'osconfig'


class AptSettings(_messages.Message):
  r"""Apt patching is completed by executing `apt-get update && apt-get
  upgrade`. Additional options can be set to control how this is executed.

  Enums:
    TypeValueValuesEnum: By changing the type to DIST, the patching is
      performed using `apt-get dist-upgrade` instead.

  Fields:
    excludes: List of packages to exclude from update. These packages will be
      excluded
    exclusivePackages: An exclusive list of packages to be updated. These are
      the only packages that will be updated. If these packages are not
      installed, they will be ignored. This field cannot be specified with any
      other patch configuration fields.
    type: By changing the type to DIST, the patching is performed using `apt-
      get dist-upgrade` instead.
  """

  class TypeValueValuesEnum(_messages.Enum):
    r"""By changing the type to DIST, the patching is performed using `apt-get
    dist-upgrade` instead.

    Values:
      TYPE_UNSPECIFIED: By default, upgrade will be performed.
      DIST: Runs `apt-get dist-upgrade`.
      UPGRADE: Runs `apt-get upgrade`.
    """
    TYPE_UNSPECIFIED = 0
    DIST = 1
    UPGRADE = 2

  excludes = _messages.StringField(1, repeated=True)
  exclusivePackages = _messages.StringField(2, repeated=True)
  type = _messages.EnumField('TypeValueValuesEnum', 3)


class CancelPatchJobRequest(_messages.Message):
  r"""Message for canceling a patch job."""


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class ExecStep(_messages.Message):
  r"""A step that runs an executable for a PatchJob.

  Fields:
    linuxExecStepConfig: The ExecStepConfig for all Linux VMs targeted by the
      PatchJob.
    windowsExecStepConfig: The ExecStepConfig for all Windows VMs targeted by
      the PatchJob.
  """

  linuxExecStepConfig = _messages.MessageField('ExecStepConfig', 1)
  windowsExecStepConfig = _messages.MessageField('ExecStepConfig', 2)


class ExecStepConfig(_messages.Message):
  r"""Common configurations for an ExecStep.

  Enums:
    InterpreterValueValuesEnum: The script interpreter to use to run the
      script. If no interpreter is specified the script will be executed
      directly, which will likely only succeed for scripts with shebang lines.
      [Wikipedia shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)).

  Fields:
    allowedSuccessCodes: Defaults to [0]. A list of possible return values
      that the execution can return to indicate a success.
    gcsObject: A GCS object containing the executable.
    interpreter: The script interpreter to use to run the script. If no
      interpreter is specified the script will be executed directly, which
      will likely only succeed for scripts with shebang lines. [Wikipedia
      shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)).
    localPath: An absolute path to the executable on the VM.
  """

  class InterpreterValueValuesEnum(_messages.Enum):
    r"""The script interpreter to use to run the script. If no interpreter is
    specified the script will be executed directly, which will likely only
    succeed for scripts with shebang lines. [Wikipedia
    shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)).

    Values:
      INTERPRETER_UNSPECIFIED: Invalid for a Windows ExecStepConfig. For a
        Linux ExecStepConfig, the interpreter will be parsed from the shebang
        line of the script if unspecified.
      SHELL: Indicates that the script is run with `/bin/sh` on Linux and
        `cmd` on Windows.
      POWERSHELL: Indicates that the file is run with PowerShell flags
        `-NonInteractive`, `-NoProfile`, and `-ExecutionPolicy Bypass`.
    """
    INTERPRETER_UNSPECIFIED = 0
    SHELL = 1
    POWERSHELL = 2

  allowedSuccessCodes = _messages.IntegerField(1, repeated=True, variant=_messages.Variant.INT32)
  gcsObject = _messages.MessageField('GcsObject', 2)
  interpreter = _messages.EnumField('InterpreterValueValuesEnum', 3)
  localPath = _messages.StringField(4)


class ExecutePatchJobRequest(_messages.Message):
  r"""A request message to initiate patching across GCE instances.

  Fields:
    description: Description of the patch job. Length of the description is
      limited to 1024 characters.
    displayName: Display name for this patch job. This does not have to be
      unique.
    dryRun: If this patch is a dry-run only, instances are contacted but will
      do nothing.
    duration: Duration of the patch job. After the duration ends, the patch
      job times out.
    instanceFilter: Required. Instances to patch, either explicitly or
      filtered by some criteria such as zone or labels.
    patchConfig: Patch configuration being applied. If omitted, instances are
      patched using the default configurations.
  """

  description = _messages.StringField(1)
  displayName = _messages.StringField(2)
  dryRun = _messages.BooleanField(3)
  duration = _messages.StringField(4)
  instanceFilter = _messages.MessageField('PatchInstanceFilter', 5)
  patchConfig = _messages.MessageField('PatchConfig', 6)


class GcsObject(_messages.Message):
  r"""GCS object representation.

  Fields:
    bucket: Required. Bucket of the GCS object.
    generationNumber: Required. Generation number of the GCS object. This is
      used to ensure that the ExecStep specified by this PatchJob does not
      change.
    object: Required. Name of the GCS object.
  """

  bucket = _messages.StringField(1)
  generationNumber = _messages.IntegerField(2)
  object = _messages.StringField(3)


class GooSettings(_messages.Message):
  r"""Googet patching is performed by running `googet update`."""


class ListPatchDeploymentsResponse(_messages.Message):
  r"""A response message for listing patch deployments.

  Fields:
    nextPageToken: A pagination token that can be used to get the next page of
      patch deployments.
    patchDeployments: The list of patch deployments.
  """

  nextPageToken = _messages.StringField(1)
  patchDeployments = _messages.MessageField('PatchDeployment', 2, repeated=True)


class ListPatchJobInstanceDetailsResponse(_messages.Message):
  r"""A response message for listing the instances details for a patch job.

  Fields:
    nextPageToken: A pagination token that can be used to get the next page of
      results.
    patchJobInstanceDetails: A list of instance status.
  """

  nextPageToken = _messages.StringField(1)
  patchJobInstanceDetails = _messages.MessageField('PatchJobInstanceDetails', 2, repeated=True)


class ListPatchJobsResponse(_messages.Message):
  r"""A response message for listing patch jobs.

  Fields:
    nextPageToken: A pagination token that can be used to get the next page of
      results.
    patchJobs: The list of patch jobs.
  """

  nextPageToken = _messages.StringField(1)
  patchJobs = _messages.MessageField('PatchJob', 2, repeated=True)


class MonthlySchedule(_messages.Message):
  r"""Represents a monthly schedule. An example of a valid monthly schedule is
  "on the third Tuesday of the month" or "on the 15th of the month".

  Fields:
    monthDay: Required. One day of the month. 1-31 indicates the 1st to the
      31st day. -1 indicates the last day of the month. Months without the
      target day will be skipped. For example, a schedule to run "every month
      on the 31st" will not run in February, April, June, etc.
    weekDayOfMonth: Required. Week day in a month.
  """

  monthDay = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  weekDayOfMonth = _messages.MessageField('WeekDayOfMonth', 2)


class OneTimeSchedule(_messages.Message):
  r"""Sets the time for a one time patch deployment. Timestamp is in <a
  href="https://www.ietf.org/rfc/rfc3339.txt" target="_blank">RFC3339</a> text
  format.

  Fields:
    executeTime: Required. The desired patch job execution time.
  """

  executeTime = _messages.StringField(1)


class OsconfigProjectsPatchDeploymentsCreateRequest(_messages.Message):
  r"""A OsconfigProjectsPatchDeploymentsCreateRequest object.

  Fields:
    parent: Required. The project to apply this patch deployment to in the
      form `projects/*`.
    patchDeployment: A PatchDeployment resource to be passed as the request
      body.
    patchDeploymentId: Required. A name for the patch deployment in the
      project. When creating a name the following rules apply: * Must contain
      only lowercase letters, numbers, and hyphens. * Must start with a
      letter. * Must be between 1-63 characters. * Must end with a number or a
      letter. * Must be unique within the project.
  """

  parent = _messages.StringField(1, required=True)
  patchDeployment = _messages.MessageField('PatchDeployment', 2)
  patchDeploymentId = _messages.StringField(3)


class OsconfigProjectsPatchDeploymentsDeleteRequest(_messages.Message):
  r"""A OsconfigProjectsPatchDeploymentsDeleteRequest object.

  Fields:
    name: Required. The resource name of the patch deployment in the form
      `projects/*/patchDeployments/*`.
  """

  name = _messages.StringField(1, required=True)


class OsconfigProjectsPatchDeploymentsGetRequest(_messages.Message):
  r"""A OsconfigProjectsPatchDeploymentsGetRequest object.

  Fields:
    name: Required. The resource name of the patch deployment in the form
      `projects/*/patchDeployments/*`.
  """

  name = _messages.StringField(1, required=True)


class OsconfigProjectsPatchDeploymentsListRequest(_messages.Message):
  r"""A OsconfigProjectsPatchDeploymentsListRequest object.

  Fields:
    pageSize: Optional. The maximum number of patch deployments to return.
      Default is 100.
    pageToken: Optional. A pagination token returned from a previous call to
      ListPatchDeployments that indicates where this listing should continue
      from.
    parent: Required. The resource name of the parent in the form
      `projects/*`.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class OsconfigProjectsPatchJobsCancelRequest(_messages.Message):
  r"""A OsconfigProjectsPatchJobsCancelRequest object.

  Fields:
    cancelPatchJobRequest: A CancelPatchJobRequest resource to be passed as
      the request body.
    name: Required. Name of the patch in the form `projects/*/patchJobs/*`
  """

  cancelPatchJobRequest = _messages.MessageField('CancelPatchJobRequest', 1)
  name = _messages.StringField(2, required=True)


class OsconfigProjectsPatchJobsExecuteRequest(_messages.Message):
  r"""A OsconfigProjectsPatchJobsExecuteRequest object.

  Fields:
    executePatchJobRequest: A ExecutePatchJobRequest resource to be passed as
      the request body.
    parent: Required. The project in which to run this patch in the form
      `projects/*`
  """

  executePatchJobRequest = _messages.MessageField('ExecutePatchJobRequest', 1)
  parent = _messages.StringField(2, required=True)


class OsconfigProjectsPatchJobsGetRequest(_messages.Message):
  r"""A OsconfigProjectsPatchJobsGetRequest object.

  Fields:
    name: Required. Name of the patch in the form `projects/*/patchJobs/*`
  """

  name = _messages.StringField(1, required=True)


class OsconfigProjectsPatchJobsInstanceDetailsListRequest(_messages.Message):
  r"""A OsconfigProjectsPatchJobsInstanceDetailsListRequest object.

  Fields:
    filter: A filter expression that filters results listed in the response.
      This field supports filtering results by instance zone, name, state, or
      `failure_reason`.
    pageSize: The maximum number of instance details records to return.
      Default is 100.
    pageToken: A pagination token returned from a previous call that indicates
      where this listing should continue from.
    parent: Required. The parent for the instances are in the form of
      `projects/*/patchJobs/*`.
  """

  filter = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  parent = _messages.StringField(4, required=True)


class OsconfigProjectsPatchJobsListRequest(_messages.Message):
  r"""A OsconfigProjectsPatchJobsListRequest object.

  Fields:
    filter: If provided, this field specifies the criteria that must be met by
      patch jobs to be included in the response. Currently, filtering is only
      available on the patch_deployment field.
    pageSize: The maximum number of instance status to return.
    pageToken: A pagination token returned from a previous call that indicates
      where this listing should continue from.
    parent: Required. In the form of `projects/*`
  """

  filter = _messages.StringField(1)
  pageSize = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(3)
  parent = _messages.StringField(4, required=True)


class PatchConfig(_messages.Message):
  r"""Patch configuration specifications. Contains details on how to apply the
  patch(es) to a VM instance.

  Enums:
    RebootConfigValueValuesEnum: Post-patch reboot settings.

  Fields:
    apt: Apt update settings. Use this setting to override the default `apt`
      patch rules.
    goo: Goo update settings. Use this setting to override the default `goo`
      patch rules.
    postStep: The `ExecStep` to run after the patch update.
    preStep: The `ExecStep` to run before the patch update.
    rebootConfig: Post-patch reboot settings.
    windowsUpdate: Windows update settings. Use this override the default
      windows patch rules.
    yum: Yum update settings. Use this setting to override the default `yum`
      patch rules.
    zypper: Zypper update settings. Use this setting to override the default
      `zypper` patch rules.
  """

  class RebootConfigValueValuesEnum(_messages.Enum):
    r"""Post-patch reboot settings.

    Values:
      REBOOT_CONFIG_UNSPECIFIED: The default behavior is DEFAULT.
      DEFAULT: The agent decides if a reboot is necessary by checking signals
        such as registry keys on Windows or `/var/run/reboot-required` on APT
        based systems. On RPM based systems, a set of core system package
        install times are compared with system boot time.
      ALWAYS: Always reboot the machine after the update completes.
      NEVER: Never reboot the machine after the update completes.
    """
    REBOOT_CONFIG_UNSPECIFIED = 0
    DEFAULT = 1
    ALWAYS = 2
    NEVER = 3

  apt = _messages.MessageField('AptSettings', 1)
  goo = _messages.MessageField('GooSettings', 2)
  postStep = _messages.MessageField('ExecStep', 3)
  preStep = _messages.MessageField('ExecStep', 4)
  rebootConfig = _messages.EnumField('RebootConfigValueValuesEnum', 5)
  windowsUpdate = _messages.MessageField('WindowsUpdateSettings', 6)
  yum = _messages.MessageField('YumSettings', 7)
  zypper = _messages.MessageField('ZypperSettings', 8)


class PatchDeployment(_messages.Message):
  r"""Patch deployments are configurations that individual patch jobs use to
  complete a patch. These configurations include instance filter, package
  repository settings, and a schedule.

  Fields:
    createTime: Output only. Time the patch deployment was created. Timestamp
      is in <a href="https://www.ietf.org/rfc/rfc3339.txt"
      target="_blank">RFC3339</a> text format.
    description: Optional. Description of the patch deployment. Length of the
      description is limited to 1024 characters.
    duration: Optional. Duration of the patch. After the duration ends, the
      patch times out.
    instanceFilter: Required. VM instances to patch.
    lastExecuteTime: Output only. The last time a patch job was started by
      this deployment. Timestamp is in <a
      href="https://www.ietf.org/rfc/rfc3339.txt" target="_blank">RFC3339</a>
      text format.
    name: Unique name for the patch deployment resource in a project. The
      patch deployment name is in the form:
      `projects/{project_id}/patchDeployments/{patch_deployment_id}`. This
      field is ignored when you create a new patch deployment.
    oneTimeSchedule: Required. Schedule a one-time execution.
    patchConfig: Optional. Patch configuration that is applied.
    recurringSchedule: Required. Schedule recurring executions.
    updateTime: Output only. Time the patch deployment was last updated.
      Timestamp is in <a href="https://www.ietf.org/rfc/rfc3339.txt"
      target="_blank">RFC3339</a> text format.
  """

  createTime = _messages.StringField(1)
  description = _messages.StringField(2)
  duration = _messages.StringField(3)
  instanceFilter = _messages.MessageField('PatchInstanceFilter', 4)
  lastExecuteTime = _messages.StringField(5)
  name = _messages.StringField(6)
  oneTimeSchedule = _messages.MessageField('OneTimeSchedule', 7)
  patchConfig = _messages.MessageField('PatchConfig', 8)
  recurringSchedule = _messages.MessageField('RecurringSchedule', 9)
  updateTime = _messages.StringField(10)


class PatchInstanceFilter(_messages.Message):
  r"""A filter to target VM instances for patching. The targeted VMs must meet
  all criteria specified. So if both labels and zones are specified, the patch
  job targets only VMs with those labels and in those zones.

  Fields:
    all: Target all VM instances in the project. If true, no other criteria is
      permitted.
    groupLabels: Targets VM instances matching at least one of these label
      sets. This allows targeting of disparate groups, for example "env=prod
      or env=staging".
    instanceNamePrefixes: Targets VMs whose name starts with one of these
      prefixes. Similar to labels, this is another way to group VMs when
      targeting configs, for example prefix="prod-".
    instances: Targets any of the VM instances specified. Instances are
      specified by their URI in the form
      `zones/[ZONE]/instances/[INSTANCE_NAME],
      `projects/[PROJECT_ID]/zones/[ZONE]/instances/[INSTANCE_NAME]`, or `http
      s://www.googleapis.com/compute/v1/projects/[PROJECT_ID]/zones/[ZONE]/ins
      tances/[INSTANCE_NAME]`
    zones: Targets VM instances in ANY of these zones. Leave empty to target
      VM instances in any zone.
  """

  all = _messages.BooleanField(1)
  groupLabels = _messages.MessageField('PatchInstanceFilterGroupLabel', 2, repeated=True)
  instanceNamePrefixes = _messages.StringField(3, repeated=True)
  instances = _messages.StringField(4, repeated=True)
  zones = _messages.StringField(5, repeated=True)


class PatchInstanceFilterGroupLabel(_messages.Message):
  r"""Represents a group of VMs that can be identified as having all these
  labels, for example "env=prod and app=web".

  Messages:
    LabelsValue: GCE instance labels that must be present for a VM instance to
      be targeted by this filter.

  Fields:
    labels: GCE instance labels that must be present for a VM instance to be
      targeted by this filter.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""GCE instance labels that must be present for a VM instance to be
    targeted by this filter.

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


class PatchJob(_messages.Message):
  r"""A high level representation of a patch job that is either in progress or
  has completed.  Instances details are not included in the job. To paginate
  through instance details, use ListPatchJobInstanceDetails.

  Enums:
    StateValueValuesEnum: The current state of the PatchJob .

  Fields:
    createTime: Time this patch job was created.
    description: Description of the patch job. Length of the description is
      limited to 1024 characters.
    displayName: Display name for this patch job. This is not a unique
      identifier.
    dryRun: If this patch job is a dry run, the agent reports that it has
      finished without running any updates on the VM instance.
    duration: Duration of the patch job. After the duration ends, the patch
      job times out.
    errorMessage: If this patch job failed, this message provides information
      about the failure.
    instanceDetailsSummary: Summary of instance details.
    instanceFilter: Instances to patch.
    name: Unique identifier for this patch job in the form
      `projects/*/patchJobs/*`
    patchConfig: Patch configuration being applied.
    patchDeployment: Output only. Name of the patch deployment that created
      this patch job.
    percentComplete: Reflects the overall progress of the patch job in the
      range of 0.0 being no progress to 100.0 being complete.
    state: The current state of the PatchJob .
    updateTime: Last time this patch job was updated.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""The current state of the PatchJob .

    Values:
      STATE_UNSPECIFIED: State must be specified.
      STARTED: The patch job was successfully initiated.
      INSTANCE_LOOKUP: The patch job is looking up instances to run the patch
        on.
      PATCHING: Instances are being patched.
      SUCCEEDED: Patch job completed successfully.
      COMPLETED_WITH_ERRORS: Patch job completed but there were errors.
      CANCELED: The patch job was canceled.
      TIMED_OUT: The patch job timed out.
    """
    STATE_UNSPECIFIED = 0
    STARTED = 1
    INSTANCE_LOOKUP = 2
    PATCHING = 3
    SUCCEEDED = 4
    COMPLETED_WITH_ERRORS = 5
    CANCELED = 6
    TIMED_OUT = 7

  createTime = _messages.StringField(1)
  description = _messages.StringField(2)
  displayName = _messages.StringField(3)
  dryRun = _messages.BooleanField(4)
  duration = _messages.StringField(5)
  errorMessage = _messages.StringField(6)
  instanceDetailsSummary = _messages.MessageField('PatchJobInstanceDetailsSummary', 7)
  instanceFilter = _messages.MessageField('PatchInstanceFilter', 8)
  name = _messages.StringField(9)
  patchConfig = _messages.MessageField('PatchConfig', 10)
  patchDeployment = _messages.StringField(11)
  percentComplete = _messages.FloatField(12)
  state = _messages.EnumField('StateValueValuesEnum', 13)
  updateTime = _messages.StringField(14)


class PatchJobInstanceDetails(_messages.Message):
  r"""Patch details for a VM instance.

  Enums:
    StateValueValuesEnum: Current state of instance patch.

  Fields:
    attemptCount: The number of times the agent that the agent attempts to
      apply the patch.
    failureReason: If the patch fails, this field provides the reason.
    instanceSystemId: The unique identifier for the instance. This identifier
      is defined by the server.
    name: The instance name in the form `projects/*/zones/*/instances/*`
    state: Current state of instance patch.
  """

  class StateValueValuesEnum(_messages.Enum):
    r"""Current state of instance patch.

    Values:
      PATCH_STATE_UNSPECIFIED: Unspecified.
      PENDING: The instance is not yet notified.
      INACTIVE: Instance is inactive and cannot be patched.
      NOTIFIED: The instance is notified that it should be patched.
      STARTED: The instance has started the patching process.
      DOWNLOADING_PATCHES: The instance is downloading patches.
      APPLYING_PATCHES: The instance is applying patches.
      REBOOTING: The instance is rebooting.
      SUCCEEDED: The instance has completed applying patches.
      SUCCEEDED_REBOOT_REQUIRED: The instance has completed applying patches
        but a reboot is required.
      FAILED: The instance has failed to apply the patch.
      ACKED: The instance acked the notification and will start shortly.
      TIMED_OUT: The instance exceeded the time out while applying the patch.
      RUNNING_PRE_PATCH_STEP: The instance is running the pre-patch step.
      RUNNING_POST_PATCH_STEP: The instance is running the post-patch step.
      NO_AGENT_DETECTED: The service could not detect the presence of the
        agent. Check to ensure that the agent is installed, running, and able
        to communicate with the service.
    """
    PATCH_STATE_UNSPECIFIED = 0
    PENDING = 1
    INACTIVE = 2
    NOTIFIED = 3
    STARTED = 4
    DOWNLOADING_PATCHES = 5
    APPLYING_PATCHES = 6
    REBOOTING = 7
    SUCCEEDED = 8
    SUCCEEDED_REBOOT_REQUIRED = 9
    FAILED = 10
    ACKED = 11
    TIMED_OUT = 12
    RUNNING_PRE_PATCH_STEP = 13
    RUNNING_POST_PATCH_STEP = 14
    NO_AGENT_DETECTED = 15

  attemptCount = _messages.IntegerField(1)
  failureReason = _messages.StringField(2)
  instanceSystemId = _messages.StringField(3)
  name = _messages.StringField(4)
  state = _messages.EnumField('StateValueValuesEnum', 5)


class PatchJobInstanceDetailsSummary(_messages.Message):
  r"""A summary of the current patch state across all instances that this
  patch job affects. Contains counts of instances in different states. These
  states map to `InstancePatchState`. List patch job instance details to see
  the specific states of each instance.

  Fields:
    ackedInstanceCount: Number of instances that have acked and will start
      shortly.
    applyingPatchesInstanceCount: Number of instances that are applying
      patches.
    downloadingPatchesInstanceCount: Number of instances that are downloading
      patches.
    failedInstanceCount: Number of instances that failed.
    inactiveInstanceCount: Number of instances that are inactive.
    noAgentDetectedInstanceCount: Number of instances that do not appear to be
      running the agent. Check to ensure that the agent is installed, running,
      and able to communicate with the service.
    notifiedInstanceCount: Number of instances notified about patch job.
    pendingInstanceCount: Number of instances pending patch job.
    postPatchStepInstanceCount: Number of instances that are running the post-
      patch step.
    prePatchStepInstanceCount: Number of instances that are running the pre-
      patch step.
    rebootingInstanceCount: Number of instances rebooting.
    startedInstanceCount: Number of instances that have started.
    succeededInstanceCount: Number of instances that have completed
      successfully.
    succeededRebootRequiredInstanceCount: Number of instances that require
      reboot.
    timedOutInstanceCount: Number of instances that exceeded the time out
      while applying the patch.
  """

  ackedInstanceCount = _messages.IntegerField(1)
  applyingPatchesInstanceCount = _messages.IntegerField(2)
  downloadingPatchesInstanceCount = _messages.IntegerField(3)
  failedInstanceCount = _messages.IntegerField(4)
  inactiveInstanceCount = _messages.IntegerField(5)
  noAgentDetectedInstanceCount = _messages.IntegerField(6)
  notifiedInstanceCount = _messages.IntegerField(7)
  pendingInstanceCount = _messages.IntegerField(8)
  postPatchStepInstanceCount = _messages.IntegerField(9)
  prePatchStepInstanceCount = _messages.IntegerField(10)
  rebootingInstanceCount = _messages.IntegerField(11)
  startedInstanceCount = _messages.IntegerField(12)
  succeededInstanceCount = _messages.IntegerField(13)
  succeededRebootRequiredInstanceCount = _messages.IntegerField(14)
  timedOutInstanceCount = _messages.IntegerField(15)


class RecurringSchedule(_messages.Message):
  r"""Sets the time for recurring patch deployments.

  Enums:
    FrequencyValueValuesEnum: Required. The frequency unit of this recurring
      schedule.

  Fields:
    endTime: Optional. The end time at which a recurring patch deployment
      schedule is no longer active.
    frequency: Required. The frequency unit of this recurring schedule.
    lastExecuteTime: Output only. The time the last patch job ran
      successfully.
    monthly: Required. Schedule with monthly executions.
    nextExecuteTime: Output only. The time the next patch job is scheduled to
      run.
    startTime: Optional. The time that the recurring schedule becomes
      effective. Defaults to `create_time` of the patch deployment.
    timeOfDay: Required. Time of the day to run a recurring deployment.
    timeZone: Required. Defines the time zone that `time_of_day` is relative
      to. The rules for daylight saving time are determined by the chosen time
      zone.
    weekly: Required. Schedule with weekly executions.
  """

  class FrequencyValueValuesEnum(_messages.Enum):
    r"""Required. The frequency unit of this recurring schedule.

    Values:
      FREQUENCY_UNSPECIFIED: Invalid. A frequency must be specified.
      WEEKLY: Indicates that the frequency should be expressed in terms of
        weeks.
      MONTHLY: Indicates that the frequency should be expressed in terms of
        months.
    """
    FREQUENCY_UNSPECIFIED = 0
    WEEKLY = 1
    MONTHLY = 2

  endTime = _messages.StringField(1)
  frequency = _messages.EnumField('FrequencyValueValuesEnum', 2)
  lastExecuteTime = _messages.StringField(3)
  monthly = _messages.MessageField('MonthlySchedule', 4)
  nextExecuteTime = _messages.StringField(5)
  startTime = _messages.StringField(6)
  timeOfDay = _messages.MessageField('TimeOfDay', 7)
  timeZone = _messages.MessageField('TimeZone', 8)
  weekly = _messages.MessageField('WeeklySchedule', 9)


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


class TimeOfDay(_messages.Message):
  r"""Represents a time of day. The date and time zone are either not
  significant or are specified elsewhere. An API may choose to allow leap
  seconds. Related types are google.type.Date and `google.protobuf.Timestamp`.

  Fields:
    hours: Hours of day in 24 hour format. Should be from 0 to 23. An API may
      choose to allow the value "24:00:00" for scenarios like business closing
      time.
    minutes: Minutes of hour of day. Must be from 0 to 59.
    nanos: Fractions of seconds in nanoseconds. Must be from 0 to 999,999,999.
    seconds: Seconds of minutes of the time. Must normally be from 0 to 59. An
      API may allow the value 60 if it allows leap-seconds.
  """

  hours = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  minutes = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  nanos = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  seconds = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class TimeZone(_messages.Message):
  r"""Represents a time zone from the [IANA Time Zone
  Database](https://www.iana.org/time-zones).

  Fields:
    id: IANA Time Zone Database time zone, e.g. "America/New_York".
    version: Optional. IANA Time Zone Database version number, e.g. "2019a".
  """

  id = _messages.StringField(1)
  version = _messages.StringField(2)


class WeekDayOfMonth(_messages.Message):
  r"""Represents one week day in a month. An example is "the 4th Sunday".

  Enums:
    DayOfWeekValueValuesEnum: Required. A day of the week.

  Fields:
    dayOfWeek: Required. A day of the week.
    weekOrdinal: Required. Week number in a month. 1-4 indicates the 1st to
      4th week of the month. -1 indicates the last week of the month.
  """

  class DayOfWeekValueValuesEnum(_messages.Enum):
    r"""Required. A day of the week.

    Values:
      DAY_OF_WEEK_UNSPECIFIED: The unspecified day-of-week.
      MONDAY: The day-of-week of Monday.
      TUESDAY: The day-of-week of Tuesday.
      WEDNESDAY: The day-of-week of Wednesday.
      THURSDAY: The day-of-week of Thursday.
      FRIDAY: The day-of-week of Friday.
      SATURDAY: The day-of-week of Saturday.
      SUNDAY: The day-of-week of Sunday.
    """
    DAY_OF_WEEK_UNSPECIFIED = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

  dayOfWeek = _messages.EnumField('DayOfWeekValueValuesEnum', 1)
  weekOrdinal = _messages.IntegerField(2, variant=_messages.Variant.INT32)


class WeeklySchedule(_messages.Message):
  r"""Represents a weekly schedule.

  Enums:
    DayOfWeekValueValuesEnum: Required. Day of the week.

  Fields:
    dayOfWeek: Required. Day of the week.
  """

  class DayOfWeekValueValuesEnum(_messages.Enum):
    r"""Required. Day of the week.

    Values:
      DAY_OF_WEEK_UNSPECIFIED: The unspecified day-of-week.
      MONDAY: The day-of-week of Monday.
      TUESDAY: The day-of-week of Tuesday.
      WEDNESDAY: The day-of-week of Wednesday.
      THURSDAY: The day-of-week of Thursday.
      FRIDAY: The day-of-week of Friday.
      SATURDAY: The day-of-week of Saturday.
      SUNDAY: The day-of-week of Sunday.
    """
    DAY_OF_WEEK_UNSPECIFIED = 0
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

  dayOfWeek = _messages.EnumField('DayOfWeekValueValuesEnum', 1)


class WindowsUpdateSettings(_messages.Message):
  r"""Windows patching is performed using the Windows Update Agent.

  Enums:
    ClassificationsValueListEntryValuesEnum:

  Fields:
    classifications: Only apply updates of these windows update
      classifications. If empty, all updates are applied.
    excludes: List of KBs to exclude from update.
    exclusivePatches: An exclusive list of kbs to be updated. These are the
      only patches that will be updated. This field must not be used with
      other patch configurations.
  """

  class ClassificationsValueListEntryValuesEnum(_messages.Enum):
    r"""ClassificationsValueListEntryValuesEnum enum type.

    Values:
      CLASSIFICATION_UNSPECIFIED: <no description>
      CRITICAL: <no description>
      SECURITY: <no description>
      DEFINITION: <no description>
      DRIVER: <no description>
      FEATURE_PACK: <no description>
      SERVICE_PACK: <no description>
      TOOL: <no description>
      UPDATE_ROLLUP: <no description>
      UPDATE: <no description>
    """
    CLASSIFICATION_UNSPECIFIED = 0
    CRITICAL = 1
    SECURITY = 2
    DEFINITION = 3
    DRIVER = 4
    FEATURE_PACK = 5
    SERVICE_PACK = 6
    TOOL = 7
    UPDATE_ROLLUP = 8
    UPDATE = 9

  classifications = _messages.EnumField('ClassificationsValueListEntryValuesEnum', 1, repeated=True)
  excludes = _messages.StringField(2, repeated=True)
  exclusivePatches = _messages.StringField(3, repeated=True)


class YumSettings(_messages.Message):
  r"""Yum patching is performed by executing `yum update`. Additional options
  can be set to control how this is executed.  Note that not all settings are
  supported on all platforms.

  Fields:
    excludes: List of packages to exclude from update. These packages are
      excluded by using the yum `--exclude` flag.
    exclusivePackages: An exclusive list of packages to be updated. These are
      the only packages that will be updated. If these packages are not
      installed, they will be ignored. This field must not be specified with
      any other patch configuration fields.
    minimal: Will cause patch to run `yum update-minimal` instead.
    security: Adds the `--security` flag to `yum update`. Not supported on all
      platforms.
  """

  excludes = _messages.StringField(1, repeated=True)
  exclusivePackages = _messages.StringField(2, repeated=True)
  minimal = _messages.BooleanField(3)
  security = _messages.BooleanField(4)


class ZypperSettings(_messages.Message):
  r"""Zypper patching is performed by running `zypper patch`. See also
  https://en.opensuse.org/SDB:Zypper_manual.

  Fields:
    categories: Install only patches with these categories. Common categories
      include security, recommended, and feature.
    excludes: List of patches to exclude from update.
    exclusivePatches: An exclusive list of patches to be updated. These are
      the only patches that will be installed using 'zypper patch
      patch:<patch_name>' command. This field must not be used with any other
      patch configuration fields.
    severities: Install only patches with these severities. Common severities
      include critical, important, moderate, and low.
    withOptional: Adds the `--with-optional` flag to `zypper patch`.
    withUpdate: Adds the `--with-update` flag, to `zypper patch`.
  """

  categories = _messages.StringField(1, repeated=True)
  excludes = _messages.StringField(2, repeated=True)
  exclusivePatches = _messages.StringField(3, repeated=True)
  severities = _messages.StringField(4, repeated=True)
  withOptional = _messages.BooleanField(5)
  withUpdate = _messages.BooleanField(6)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
