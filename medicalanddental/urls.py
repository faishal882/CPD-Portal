from django.urls import path

from .views import (portal_view,
                    csv_export,
                    excel_export, 
                    participants_view, 
                    history_view, 
                    excel_upload)

app_name = "medicalanddental"

urlpatterns = [
    path('portal/', portal_view, name='portal'),
    path('participants/', participants_view, name='participants'),
    path('history/', history_view, name='history'),
    path('export/csv/', csv_export, name='csv-export'),
    path('export/excel/', excel_export, name='excel-export'),
    path('upload/excel/', excel_upload, name='excel-upload'),
]