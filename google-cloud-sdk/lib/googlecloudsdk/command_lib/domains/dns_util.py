# -*- coding: utf-8 -*- #
# Copyright 2020 Google LLC. All Rights Reserved.
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
"""DNS utilties for Cloud Domains commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import sys

from apitools.base.py import exceptions as apitools_exceptions

from googlecloudsdk.api_lib.dns import util as dns_api_util
from googlecloudsdk.api_lib.domains import registrations
from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.calliope import exceptions as calliope_exceptions
from googlecloudsdk.command_lib.domains import util
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core.console import console_io
from googlecloudsdk.core.resource import resource_printer
import six


class DnsUpdateMask(object):
  """Class with information which parts of dns_settings should be updated."""

  def __init__(self,
               dns_provider=False,
               glue_records=False,
               google_domains_dnssec=False,
               custom_dnssec=False):
    self.dns_provider = dns_provider
    self.glue_records = glue_records
    self.google_domains_dnssec = google_domains_dnssec
    self.custom_dnssec = custom_dnssec


def ParseDNSSettings(name_servers,
                     cloud_dns_zone,
                     use_google_domains_dns,
                     dns_settings_from_file,
                     domain,
                     enable_dnssec=True,
                     dns_settings=None):
  """Parse DNS settings from a flag.

  At most one of the arguments (except domain) should be non-empty.

  Args:
    name_servers: List of name servers
    cloud_dns_zone: Cloud DNS Zone name
    use_google_domains_dns: Information that Google Domains name servers should
      be used.
    dns_settings_from_file: Path to a yaml file with dns_settings.
    domain: Domain name corresponding to the DNS settings.
    enable_dnssec: Enable DNSSEC for Google Domains name servers or Cloud DNS
      Zone.
    dns_settings: Current DNS settings. Used during Configure DNS only.

  Returns:
    A pair: (messages.DnsSettings, DnsUpdateMask) to be updated, or (None, None)
    if all the arguments are empty.
  """
  if name_servers is not None:
    return _CustomNameServers(name_servers)
  if cloud_dns_zone is not None:
    nameservers, ds_records = _GetCloudDnsDetails(cloud_dns_zone, domain,
                                                  enable_dnssec)
    return _CustomNameServers(nameservers, ds_records)
  if use_google_domains_dns:
    return _GoogleDomainsNameServers(enable_dnssec)
  if dns_settings_from_file is not None:
    return _ParseDnsSettingsFromFile(dns_settings_from_file)
  if dns_settings is not None and not enable_dnssec:
    return _DisableDnssec(dns_settings)
  return None, None


def _CustomNameServers(name_servers, ds_records=None):
  if not ds_records:
    ds_records = []
  messages = registrations.GetMessagesModule()
  update_mask = DnsUpdateMask(dns_provider=True)
  dns_settings = messages.DnsSettings(
      customDns=messages.CustomDns(
          nameServers=name_servers, dsRecords=ds_records))
  return dns_settings, update_mask


def _GoogleDomainsNameServers(enable_dnssec):
  messages = registrations.GetMessagesModule()

  update_mask = DnsUpdateMask(dns_provider=True)
  ds_state = messages.GoogleDomainsDns.DsStateValueValuesEnum.DS_RECORDS_PUBLISHED
  if not enable_dnssec:
    ds_state = messages.GoogleDomainsDns.DsStateValueValuesEnum.DS_RECORDS_UNPUBLISHED
  dns_settings = messages.DnsSettings(
      googleDomainsDns=messages.GoogleDomainsDns(dsState=ds_state))
  return dns_settings, update_mask


def _ParseDnsSettingsFromFile(path):
  """Parse dns_settings from a yaml file.

  Args:
    path: YAML file path.

  Returns:
    Pair (DnsSettings, DnsUpdateMask) or (None, None) if path is None.
  """
  messages = registrations.GetMessagesModule()
  dns_settings = util.ParseMessageFromYamlFile(
      path, messages.DnsSettings,
      'DNS settings file \'{}\' does not contain valid dns_settings message'
      .format(path))
  if not dns_settings:
    return None, None

  return dns_settings, DnsUpdateMask(dns_provider=True, glue_records=True)


def _GetCloudDnsDetails(cloud_dns_zone, domain, enable_dnssec):
  """Fetches list of name servers from provided Cloud DNS Managed Zone.

  Args:
    cloud_dns_zone: Cloud DNS Zone resource reference.
    domain: Domain name.
    enable_dnssec: If true, try to read DNSSEC information from the Zone.

  Returns:
    A pair: List of name servers and a list of Ds reocrds (or [] if e.g. the
    Zone is not signed).
  """
  # Get the managed-zone.
  dns_api_version = 'v1'
  dns = apis.GetClientInstance('dns', dns_api_version)
  zone_ref = dns_api_util.GetRegistry(dns_api_version).Parse(
      cloud_dns_zone,
      params={
          'project': properties.VALUES.core.project.GetOrFail,
      },
      collection='dns.managedZones')

  try:
    zone = dns.managedZones.Get(
        dns.MESSAGES_MODULE.DnsManagedZonesGetRequest(
            project=zone_ref.project, managedZone=zone_ref.managedZone))
  except apitools_exceptions.HttpError as error:
    raise calliope_exceptions.HttpException(error)
  domain_with_dot = domain + '.'
  if zone.dnsName != domain_with_dot:
    raise exceptions.Error(
        'The dnsName \'{}\' of specified Cloud DNS zone \'{}\' does not match the '
        'registration domain \'{}\''.format(zone.dnsName, cloud_dns_zone,
                                            domain_with_dot))
  if zone.visibility != dns.MESSAGES_MODULE.ManagedZone.VisibilityValueValuesEnum.public:
    raise exceptions.Error(
        'Cloud DNS Zone \'{}\' is not public.'.format(cloud_dns_zone))

  if not enable_dnssec:
    return zone.nameServers, []

  signed = dns.MESSAGES_MODULE.ManagedZoneDnsSecConfig.StateValueValuesEnum.on
  if not zone.dnssecConfig or zone.dnssecConfig.state != signed:
    log.status.Print(
        'Cloud DNS Zone \'{}\' is not signed. DNSSEC won\'t be enabled.'.format(
            cloud_dns_zone))
    return zone.nameServers, []
  try:
    dns_keys = []
    req = dns.MESSAGES_MODULE.DnsDnsKeysListRequest(
        project=zone_ref.project,
        managedZone=zone_ref.managedZone,
        maxResults=1)
    while True:
      resp = dns.dnsKeys.List(
          dns.MESSAGES_MODULE.DnsDnsKeysListRequest(
              project=zone_ref.project, managedZone=zone_ref.managedZone))
      dns_keys += resp.dnsKeys
      req.pageToken = resp.nextPageToken
      if not resp.nextPageToken:
        break
  except apitools_exceptions.HttpError as error:
    log.status.Print('Cannot read DS records from Cloud DNS Zone \'{}\': {}. '
                     'DNSSEC won\'t be enabled.'.format(cloud_dns_zone, error))
  ds_records = _ConvertDnsKeys(dns.MESSAGES_MODULE, dns_keys)
  if not ds_records:
    log.status.Print('No supported DS records found in Cloud DNS Zone \'{}\'. '
                     'DNSSEC won\'t be enabled.'.format(cloud_dns_zone))
    return zone.nameServers, []
  return zone.nameServers, ds_records


def _ConvertDnsKeys(dns_messages, dns_keys):
  """Convert DnsKeys to DsRecords."""
  messages = registrations.GetMessagesModule()
  ds_records = []
  for key in dns_keys:
    if key.type != dns_messages.DnsKey.TypeValueValuesEnum.keySigning:
      continue
    if not key.isActive:
      continue
    try:
      algorithm = messages.DsRecord.AlgorithmValueValuesEnum(
          six.text_type(key.algorithm).upper())
      for d in key.digests:
        digest_type = messages.DsRecord.DigestTypeValueValuesEnum(
            six.text_type(d.type).upper())
        ds_records.append(
            messages.DsRecord(
                keyTag=key.keyTag,
                digest=d.digest,
                algorithm=algorithm,
                digestType=digest_type))
    except TypeError:
      continue  # Ignore unsupported algorithms and digest types.
  return ds_records


def _DisableDnssec(dns_settings):
  """Returns DNS settings (and update mask) with DNSSEC disabled."""
  if dns_settings is None:
    return None, None
  messages = registrations.GetMessagesModule()
  if dns_settings.googleDomainsDns is not None:
    updated_dns_settings = messages.DnsSettings(
        googleDomainsDns=messages.GoogleDomainsDns(
            dsState=messages.GoogleDomainsDns.DsStateValueValuesEnum
            .DS_RECORDS_UNPUBLISHED))
    update_mask = DnsUpdateMask(google_domains_dnssec=True)
  elif dns_settings.customDns is not None:
    updated_dns_settings = messages.DnsSettings(
        customDns=messages.CustomDns(dsRecords=[]))
    update_mask = DnsUpdateMask(custom_dnssec=True)
  else:
    return None, None
  return updated_dns_settings, update_mask


def PromptForNameServers(domain,
                         enable_dnssec=None,
                         dns_settings=None,
                         print_format='default'):
  """Ask the user to provide DNS settings interactively.

  Args:
    domain: Domain name corresponding to the DNS settings.
    enable_dnssec: Should the DNSSEC be enabled.
    dns_settings: Current DNS configuration (or None if resource is not yet
      created).
    print_format: Print format to use when showing current dns_settings.

  Returns:
    A pair: (messages.DnsSettings, DnsUpdateMask) to be updated, or (None, None)
    if the user cancelled.
  """
  options = [
      'Provide name servers list', 'Provide Cloud DNS Managed Zone name',
      'Use free name servers provided by Google Domains'
  ]
  if dns_settings is not None:
    log.status.Print('Your current DNS settings are:')
    resource_printer.Print(dns_settings, print_format, out=sys.stderr)

    cancel_option = True
    default = len(options)  # Additional 'cancel' option.
  else:
    cancel_option = False
    default = 1  # Cloud DNS Zone.

  message = ('You can provide your DNS settings by specifying name servers, '
             'Cloud DNS Managed Zone name or by choosing '
             'free name servers provided by Google Domains')
  index = console_io.PromptChoice(
      message=message,
      options=options,
      cancel_option=cancel_option,
      default=default)
  name_servers = []
  if index == 0:  # name servers.
    while len(name_servers) < 2:
      while True:
        ns = console_io.PromptResponse('Name server (empty line to finish):  ')
        if not ns:
          break
        if not util.ValidateDomainName(ns):
          log.status.Print('Invalid name server: \'{}\'.'.format(ns))
        else:
          name_servers += [ns]
      if len(name_servers) < 2:
        log.status.Print('You have to provide at least 2 name servers.')
    return _CustomNameServers(name_servers)
  elif index == 1:  # Cloud DNS.
    while True:
      zone = util.PromptWithValidator(
          validator=util.ValidateNonEmpty,
          error_message=' Cloud DNS Managed Zone name must not be empty.',
          prompt_string='Cloud DNS Managed Zone name:  ')
      try:
        name_servers, ds_records = _GetCloudDnsDetails(zone, domain,
                                                       enable_dnssec)
      except (exceptions.Error, calliope_exceptions.HttpException) as e:
        log.status.Print(six.text_type(e))
      else:
        break
    return _CustomNameServers(name_servers, ds_records)
  elif index == 2:  # Google Domains name servers.
    return _GoogleDomainsNameServers(enable_dnssec)
  else:
    return None, None  # Cancel.


def NameServersEquivalent(prev_dns_settings, new_dns_settings):
  if prev_dns_settings.googleDomainsDns:
    return bool(new_dns_settings.googleDomainsDns)
  if prev_dns_settings.customDns:
    if not new_dns_settings.customDns:
      return False
    return prev_dns_settings.customDns.nameServers == new_dns_settings.customDns.nameServers

  return False


def PromptForUnsafeDnsUpdate():
  console_io.PromptContinue(
      'This operation is not safe.',
      default=False,
      throw_if_unattended=True,
      cancel_on_no=True)


def DnssecEnabled(dns_settings):
  ds_records = []
  if dns_settings.googleDomainsDns is not None:
    ds_records = dns_settings.googleDomainsDns.dsRecords
  if dns_settings.customDns is not None:
    ds_records = dns_settings.customDns.dsRecords
  return bool(ds_records)
