from django.contrib import admin
from .models import MeetingType, MeetingMinutes, MeetingResource, MeetingEvent

# Register your models here.
admin.site.register(MeetingType)
admin.site.register(MeetingMinutes)
admin.site.register(MeetingResource)
admin.site.register(MeetingEvent)
