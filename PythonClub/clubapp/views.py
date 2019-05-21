from django.shortcuts import render, get_object_or_404
from .models import MeetingType, MeetingMinutes, MeetingResource, MeetingEvent
from .forms import MeetingForm
from django.contrib.auth.decorators import login_required

def index (request):
    return render(request, 'clubapp/index.html')

def getypes (request):
    types_list = MeetingType.objects.all()
    context={"types_list" : types_list}
    return render (request, 'clubapp/types.html', context=context)

def getMeetings (request):
    resources_list=MeetingTypes.objects.all()
    return render (request, 'clubapp/meetings.html'), {'meeting_list': meeting_list}

def meetingsAgenda (request, id):
     prod=Meetings.agenda.get (pk=id)
     agenda=Meetings.agenda.filter(meeting=id)
     context={
     'prod' : prod,
     }

     return render (request, "clubapp/resoucedetail.html", context = context)
     

def newmeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'clubapp/newmeeting.html', {'form' : form})

@login_required
def newMeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'clubapp/newmeeting.html', {'form': form})
