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

"""Utilities for expanding wildcarded GCS pathnames."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import abc

from googlecloudsdk.api_lib.storage import gcs_api
from googlecloudsdk.command_lib.storage import resource_reference
from googlecloudsdk.command_lib.storage import storage_url
import six


class WildcardIterator(six.with_metaclass(abc.ABCMeta)):
  """Class for iterating over Google Cloud Storage strings containing wildcards.

  The base class is abstract; you should instantiate using the
  wildcard_iterator() static factory method, which chooses the right
  implementation depending on the base string.
  """

  def __repr__(self):
    """Returns string representation of WildcardIterator."""
    return 'WildcardIterator(%s)' % self.wildcard_url.url_string


class CloudWildcardIterator(WildcardIterator):
  """Class to iterate over Cloud Storage strings containing wildcards."""

  def __init__(self, url_str, all_versions=False):
    """Instantiates an iterator that matches the wildcard URL.

    Args:
      url_str (str): CloudUrl that may contain wildcard that needs expansion.
      all_versions (bool): If true, the iterator yields all versions of objects
        matching the wildcard.  If false, yields just the live object version.
    """
    super(CloudWildcardIterator, self).__init__()
    self._url_str = url_str
    self._all_versions = all_versions
    self._client = gcs_api.GcsApi()

  def __iter__(self):
    url = storage_url.storage_url_from_string(self._url_str)
    if url.is_provider():
      for bucket in self._client.ListBuckets():
        yield resource_reference.BucketReference(url, bucket)
