from django.urls import path

from .views import (portal_view,
                    login_view, 
                    register_user_view, 
                    csv_export, excel_export, 
                    participants_view, 
                    history_view)



urlpatterns = [
    path('portal/', portal_view, name='portal'),
    path('participants/', participants_view, name='participants'),
    path('history/', history_view, name='history'),
    path('login/', login_view, name='login'),
    path('register/', register_user_view, name='register-user'),
    path('export/csv/', csv_export, name='csv-export'),
    path('export/excel/', excel_export, name='excel-export'),
    # path('upload/excel/', excel_upload, name='excel-upload'),
]