from django.urls import path

from .views import profile_update_view, profile_api_view

app_name = "participants"

urlpatterns = [
    path('update/', profile_update_view, name="profile-update-view"),
    path('api/profiles/', profile_api_view, name="profile-api-view"),
]
