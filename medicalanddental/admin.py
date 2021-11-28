from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import MedicalDentalCouncil

class ExportDataAdmin(ImportExportModelAdmin):
    list_display = [ 'Username', 'CourseTitle', 'MdcPinNumber', 'CertificateNumber', 'DateOfCompletion', 'Course', 'EntryTime', 'EntryDate' ]
    show_full_result_count = True
    empty_value_display = '-empty-'



admin.site.register(MedicalDentalCouncil, ExportDataAdmin)
