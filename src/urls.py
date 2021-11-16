from django.contrib import admin
from django.urls import path
from export.views import csv_export, excel_export

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export/csv/', csv_export, name='csv-eport'),
    path('export/excel/', excel_export, name='excel-eport'),
]
