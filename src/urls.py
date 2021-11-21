from django.contrib import admin
from django.urls import path
from export.views import csv_export, excel_export, home_view, portal_view, login_view, register_user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('portal/', portal_view, name='portal'),
    path('login/', login_view, name='login'),
     path('register/', register_user_view, name='register-user'),
    path('export/csv/', csv_export, name='csv-export'),
    path('export/excel/', excel_export, name='excel-export'),
]
