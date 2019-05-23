from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clubapp/', include ('clubapp.urls')),
    path ('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('clubapp/', include('clubapp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
