from django import forms
from .models import MeetingType, MeetingMinutes, MeetingResource, MeetingEvent
class MeetingForm(forms.ModelForm):
    class Meta:
        model=MeetingType
        fields='__all__'