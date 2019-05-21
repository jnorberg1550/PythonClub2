from django.urls import path
from .import views 

urlpatterns = [
    path ('', views.index, name = 'index'),
    path ('gettypes/', views.getypes, name = 'types'),
    path ('newMeeting/<int:id>', views.newMeeting, name = 'newmeeting'),
    
]