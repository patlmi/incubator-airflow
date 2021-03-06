# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime, timedelta
import unittest

from airflow.utils import dates


class Dates(unittest.TestCase):

    def test_days_ago(self):
        today = datetime.today()
        today_midnight = datetime.fromordinal(today.date().toordinal())

        self.assertTrue(dates.days_ago(0) == today_midnight)

        self.assertTrue(
            dates.days_ago(100) == today_midnight + timedelta(days=-100))

        self.assertTrue(
            dates.days_ago(0, hour=3) == today_midnight + timedelta(hours=3))
        self.assertTrue(
            dates.days_ago(0, minute=3)
            == today_midnight + timedelta(minutes=3))
        self.assertTrue(
            dates.days_ago(0, second=3)
            == today_midnight + timedelta(seconds=3))
        self.assertTrue(
            dates.days_ago(0, microsecond=3)
            == today_midnight + timedelta(microseconds=3))
