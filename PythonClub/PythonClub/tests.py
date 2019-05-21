from django.test import TestCase
from django.contrib auth.models.User
from django.urls import reverse
from models import MeetingType, MeetingMinutes, MeetingResource, MeetingEvent

class MeetingTypeTest(TestCase):
    def test_string(self):
        type = MeetingType (meetingtitle = 'review')
        self.assertEqual(str(MeetingType), type.meetingtitle)

    def test_string(self):
        self.assertEqual(str(MeetingType.meta.db_table), 'meetingtype')

class MeetingTypeTest(TestCase):
    def setup(self)
    Type = MeetingResource(resourcetype = 'whiteboard', resourcedescription = self.type, resourcentrydate = ('April 6 2019'))

class GetMeetingTest (Testcase):
    def setUp(self):
        self.u.objects.create  = User (username = 'myUser')
        self.MeetingType.objects.create = meetingagenda = 'performance review'



