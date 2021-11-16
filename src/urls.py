from django.contrib import admin
from django.urls import path
from export.views import csv_export, excel_export, home_view, api_view_excel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('export/csv/', csv_export, name='csv-export'),
    path('export/excel/', excel_export, name='excel-export'),
    path('api/excel-data/', api_view_excel, name='api-view-excel'),
]
