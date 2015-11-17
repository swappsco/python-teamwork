from unittest import TestCase
from datetime import timedelta, time
import teamwork
import inspect


class TestTeamwork(TestCase):
    def test_class_exists(self):
        self.assertTrue(inspect.isclass(teamwork.Teamwork))

    def test_timedelta_to_hours_minutes(self):
        duration = timedelta(hours=1, minutes=10)
        hours, minutes = teamwork.timedelta_to_hours_minutes(duration)
        self.assertEqual(hours, 1)
        self.assertEqual(minutes, 10)

    def test_time_to_hhmm(self):
        entry_time = teamwork.time_to_hhmm(time(8, 45))
        self.assertEqual(entry_time, '8:45')
