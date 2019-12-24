# -*- coding: utf-8 -*- #
# Copyright 2018 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Dynamic context for connection to Serverless."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import abc
import contextlib
import ssl
import sys
from googlecloudsdk.api_lib.serverless import gke
from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.command_lib.serverless import exceptions as serverless_exceptions
from googlecloudsdk.command_lib.serverless import flags

from googlecloudsdk.core import properties

import six
from six.moves.urllib import parse as urlparse


_SERVERLESS_API_NAME = 'serverless'
_SERVERLESS_API_VERSION = 'v1alpha1'


@contextlib.contextmanager
def _OverrideEndpointOverrides(override):
  """Context manager to override the Serverless endpoint overrides for a while.

  Args:
    override: str, New value for serverless endpoint.
  Yields:
    None.
  """
  old_endpoint = properties.VALUES.api_endpoint_overrides.serverless.Get()
  try:
    properties.VALUES.api_endpoint_overrides.serverless.Set(override)
    yield
  finally:
    properties.VALUES.api_endpoint_overrides.serverless.Set(old_endpoint)


class ConnectionInfo(six.with_metaclass(abc.ABCMeta)):
  """Information useful in constructing an API client."""

  def __init__(self):
    self.endpoint = None
    self.ca_certs = None
    self._cm = None

  @property
  def api_name(self):
    return _SERVERLESS_API_NAME

  @property
  def api_version(self):
    return _SERVERLESS_API_VERSION

  @abc.abstractmethod
  def Connect(self):
    pass

  @abc.abstractproperty
  def ns_label(self):
    pass

  @abc.abstractproperty
  def location_label(self):
    pass

  def __enter__(self):
    self._cm = self.Connect()
    return self._cm.__enter__()

  def __exit__(self, typ, value, traceback):
    return self._cm.__exit__(typ, value, traceback)


def _CheckTLSSupport():
  # PROTOCOL_TLSv1_2 applies to [2.7.9, 2.7.13) or [3.4, 3.6).
  # PROTOCOL_TLS applies to 2.7.13 and above, or 3.6 and above.
  if not (hasattr(ssl, 'PROTOCOL_TLS') or hasattr(ssl, 'PROTOCOL_TLSv1_2')):
    min_required_version = ('2.7.9' if sys.version_info.major == 2 else '3.4')
    raise serverless_exceptions.NoTLSError(
        'Your Python {}.{}.{} installation does not support TLS 1.2, which is'
        ' required to connect to the GKE Serverless add-on. Please upgrade to'
        ' Python {} or greater.'.format(
            sys.version_info.major,
            sys.version_info.minor,
            sys.version_info.micro,
            min_required_version))


class _GKEConnectionContext(ConnectionInfo):
  """Context manager to connect to the GKE Serverless add-in."""

  def __init__(self, cluster_ref):
    super(_GKEConnectionContext, self).__init__()
    self.cluster_ref = cluster_ref

  @property
  def ns_label(self):
    return 'namespace'

  @property
  def location_label(self):
    return ' of cluster [{{{{bold}}}}{}{{{{bold}}}}]'.format(
        self.cluster_ref.Name())

  @contextlib.contextmanager
  def Connect(self):
    _CheckTLSSupport()
    with gke.ClusterConnectionInfo(self.cluster_ref) as (ip, ca_certs):
      self.ca_certs = ca_certs
      with gke.MonkeypatchAddressChecking('kubernetes.default', ip) as endpoint:
        self.endpoint = 'https://{}/'.format(endpoint)
        with _OverrideEndpointOverrides(self.endpoint):
          yield self


class _RegionalConnectionContext(ConnectionInfo):
  """Context manager to connect a particular Serverless region."""

  def __init__(self, region):
    super(_RegionalConnectionContext, self).__init__()
    self.region = region

  @property
  def ns_label(self):
    return 'project'

  @property
  def location_label(self):
    return ''

  @contextlib.contextmanager
  def Connect(self):
    global_endpoint = apis.GetEffectiveApiEndpoint(_SERVERLESS_API_NAME,
                                                   _SERVERLESS_API_VERSION)
    scheme, netloc, path, params, query, fragment = urlparse.urlparse(
        global_endpoint)
    netloc = '{}-{}'.format(self.region, netloc)
    self.endpoint = urlparse.urlunparse(
        (scheme, netloc, path, params, query, fragment))
    with _OverrideEndpointOverrides(self.endpoint):
      yield self


def GetConnectionContext(args):
  """Gets the regional or GKE connection context.

  Args:
    args: Namespace, the args namespace.

  Raises:
    ConfigurationError if cluster is specified without a location.

  Returns:
    A GKE or regional ConnectionInfo object.
  """

  cluster_ref = args.CONCEPTS.cluster.Parse()
  if cluster_ref:
    return _GKEConnectionContext(cluster_ref)

  flags.ValidateClusterArgs(args)
  region = flags.GetRegion(args, prompt=True)
  if not region:
    raise flags.ArgumentError('You must specify either a cluster or a region.')
  return _RegionalConnectionContext(region)
