from django.urls import path

from .views import profile_update_view

app_name = "participants"

urlpatterns = [
    path('update/', profile_update_view),
]
