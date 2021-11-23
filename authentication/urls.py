from django.urls import path
from .views import user_register_view, login_view, logout_view

app_name = "authentication"

urlpatterns = [
    path('register/', user_register_view, name='user-register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
