# -*- coding: utf-8 -*- #
# Copyright 2020 Google Inc. All Rights Reserved.
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
"""API Keys API helper functions."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import list_pager
from googlecloudsdk.api_lib.util import apis

_PROJECT_RESOURCE = 'projects/%s'


def ListKeys(project, deleted=None, page_size=None, limit=None):
  """List API Keys for a given project.

  Args:
    project: The project for which to list keys.
    deleted: List deleted keys.
    page_size: The page size to list.
    limit: The max number of metrics to return.

  Raises:
    exceptions.PermissionDeniedException: when listing keys fails.

  Returns:
    The list of keys
  """
  client = _GetClientInstance()
  messages = client.MESSAGES_MODULE

  if deleted:
    key_filter = 'state:DELETED'
  else:
    key_filter = None
  request = messages.ApikeysProjectsKeysListRequest(
      parent=_PROJECT_RESOURCE % (project), filter=key_filter)
  return list_pager.YieldFromList(
      client.projects_keys,
      request,
      limit=limit,
      batch_size_attribute='pageSize',
      batch_size=page_size,
      field='keys')


def _GetClientInstance():
  return apis.GetClientInstance('apikeys', 'v2alpha1')
