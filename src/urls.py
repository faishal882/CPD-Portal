from django.contrib import admin
from django.urls import path, include
from medicalanddental.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('auth/', include('authentication.urls')),
    path('participants/', include('participants.urls')),
    path('medical/', include('medicalanddental.urls')),
]
