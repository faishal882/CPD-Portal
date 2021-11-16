from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import ExportData

class ExportDataAdmin(ImportExportModelAdmin):
    list_display = [ 'Name', 'CourseTitle', 'MdcPinNumber', 'CertificateNumber', 'DateOfCompletion', 'Type' ]
    show_full_result_count = True
    empty_value_display = '-empty-'



admin.site.register(ExportData, ExportDataAdmin)