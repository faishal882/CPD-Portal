from django.contrib import admin
from django.urls import path
from export.views import csv_export, excel_export, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('export/csv/', csv_export, name='csv-export'),
    path('export/excel/', excel_export, name='excel-export'),
]
