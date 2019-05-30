from django.test import TestCase
from django.contrib auth.models.User
from django.urls import reverse
from models import MeetingType, MeetingMinutes, MeetingResource, MeetingEvent
import datetime
from .forms import MeetingForm

class MeetingTypeTest(TestCase):
    def test_string(self):
        type = MeetingType (meetingtitle = 'review')
        self.assertEqual(str(MeetingType), type.meetingtitle)

    def test_string(self):
        type = MeetingType (meetingdate = '4-26-2019')
        self.assertEqual(str(MeetingType), type.meetingdate)

    def test_string(self):
        type = MeetingType (meetinglocation = 'Room 210')
        self.assertEqual(str(MeetingType), type.location)

     def test_string(self):
        type = MeetingType (meetingagenda = 'Plan test strategy')
        self.assertEqual(str(MeetingType), type.meetingagenda)
    def test_string(self):
        self.assertEqual(str(MeetingType.meta.db_table), 'meetingtype')

    class MeetingMinutesTest(TestCase):
        def test_string(self):
        type = MeetingMinutes (minutesid = '100')
        self.assertEqual(str(MeetingMinutes), type.minutesid)

        def test_string(self):
        type = MeetingMinutes (minutesattendance = 'Tom')
        self.assertEqual(str(MeetingMinutes), type.minutesattendance)

        def test_string(self):
        type = MeetingMinutes (minutestext = 'Bug report')
        self.assertEqual(str(MeetingMinutes), type.minutestext)

        def test_string(self):
        self.assertEqual(str(MeetingMinutes.meta.db_table), 'meetingminutes')


   class MeetingResourceTest(TestCase):
        def test_string(self):
        type = MeetingResource (resourcename = 'printer')
        self.assertEqual(str(MeetingResource), type.resourcename)
        
        def test_string(self):
        type = MeetingResource (resourcetype = 'HP')
        self.assertEqual(str(MeetingResource), type.resourcetype) 
        
        def test_string(self):
        type = MeetingResource (resourceurl = 'https://canvas.seattlecentral.edu/courses/1759075/assignments/14766750')
        self.assertEqual(str(MeetingResource), type.resourceurl) 
        
        def test_string(self):
        type = MeetingResource (resourceentrydate = '4-22-2019')
        self.assertEqual(str(MeetingResource), type.resourceentrydate)
       
        def test_string(self):
        type = MeetingResource (resourceuser = 'Jill')
        self.assertEqual(str(MeetingResource), type.resourceuser)

         def test_string(self):
        type = MeetingResource (resourcedescription = 'color printer')
        self.assertEqual(str(MeetingResource), type.resourcedescription) 
        
        def test_string(self):
        self.assertEqual(str(MeetingResource.meta.db_table), 'meetingresource')     

    class MeetingEventTest(TestCase):
        def test_string(self):
        type = MeetingEvent (eventtitle = 'design review')
        self.assertEqual(str(MeetingEvent), type.eventtitle)

    def test_string(self):
        type = MeetingEvent (eventlocation = 'Main Office')
        self.assertEqual(str(MeetingEvent), type.eventlocation)

    def test_string(self):
        type = MeetingEvent (eventdate = '5-10-2019')
        self.assertEqual(str(MeetingEvent), type.eventdate)

    def test_string(self):
        type = MeetingEvent (eventtime = '13:30')
        self.assertEqual(str(MeetingEvent), type.eventime)

    def test_string(self):
        type = MeetingEvent (eventdescription = 'review')
        self.assertEqual(str(MeetingEvent), type.eventdescription)

    def test_string(self):
        type = MeetingEvent (eventuserid = 'jnorberg')
        self.assertEqual(str(MeetingEvent), type.eventuserid)

    def test_string(self):
        self.assertEqual(str(MeetingEvent.meta.db_table), 'meetingevent')     

class MeetingFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username = 'Larry', password = 'P@ssw0rd1')
        self.type=MeetingType.objects.create(meetingtypename = 'type1')

    def test_MeetingForm(self):
        data={
            'meetingtitle' : 'codereview',
            'meetingdate' :  datetime.date(2019,5,26),
            'meetingtime' :  datetime.time(13,15),
            'meetinglocation' : 'Room 126',
            'meetingagenda' : self.meetingagenda,
        }
        form=MeetingForm(data=data)
        self.assertTrue(form.is_valid())
