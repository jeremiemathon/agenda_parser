#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line sample for the Calendar API.
Command-line application that retrieves the list of the user's calendars."""

import sys
import pytz
import pprint

from datetime import datetime, timedelta
from oauth2client import client
from googleapiclient import sample_tools
from base_functions import list_actions 


def print_actions(events):
	for i in events["items"]:
		try:
			start = datetime.strptime(str(i["start"]["dateTime"])[:-6], "%Y-%m-%dT%H:%M:%S")
			end = datetime.strptime(str(i["end"]["dateTime"])[:-6], "%Y-%m-%dT%H:%M:%S")
			value = str(i["summary"])
			duration = end - start
			#print(duration)
			print(str('%-20s' % start) + "\t" + str('%-50s' % value) + "\t" + str('%-20s' % end))
		except KeyError:
			continue

def total_duration(events):
	total = timedelta()
	for i in events["items"]:
		try:
			start = datetime.strptime(str(i["start"]["dateTime"])[:-6], "%Y-%m-%dT%H:%M:%S")
			end = datetime.strptime(str(i["end"]["dateTime"])[:-6], "%Y-%m-%dT%H:%M:%S")
			duration = end - start
			total = total + duration
		except KeyError:
			continue
		print(total)

if __name__ == '__main__':
	events = list_actions(sys.argv)
	print_actions(events)
