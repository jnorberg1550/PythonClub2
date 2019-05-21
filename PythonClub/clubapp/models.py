
from django.db import models
from django.contrib.auth.models import User



class MeetingType(models.Model):
    meetingtitle=models.CharField (max_length=64)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField (max_length=255)
    meetingagenda=models.CharField (max_length=255)
 
    class Meta:
        db_table='meetings'
        verbose_name_plural='MeetingTypes'

    def __str__(self):
        return self.meetingtitle

class MeetingMinutes(models.Model):
    minutesid=models.ForeignKey (MeetingType, on_delete = models.DO_NOTHING)
    minutesattendance=models.ManyToManyField(User)
    minutestext=models.TextField()

    class Meta:
        db_table= 'minutes'
        verbose_name_plural='MeetingMinutes'

    def __str__(self):
        return self.minutesid

class MeetingResource(models.Model):
    resourcename=models.CharField (max_length=64)
    resourcetype=models.CharField (max_length=64)
    resourceurl=models.URLField(null=True, blank=True)
    resourceentrydate=models.DateField()
    resourceuserid=models.ForeignKeyField(User, on_delete=models.CASCADE)
    resourcedescription=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table= 'resource'
        verbose_name_plural='MeetingResources'
   


class MeetingEvent (models.Model):
    eventtitle=models.CharField (max_length=64)
    eventlocation=models.CharField (max_length=64)
    eventdate=models.DateField()
    eventtime=models.TimeField ()
    eventdescription=models.TextField()
    eventuserid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    
    class Meta:
        db_table= 'events'
        verbose_name_plural='MeetingEvents'


    def __str__(self):
        return self.eventtitle

# Register your models here.







