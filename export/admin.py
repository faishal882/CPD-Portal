from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import ExportData

class ExportDataAdmin(ImportExportModelAdmin):
    list_dispaly = ('Name', 'CourseTitle', 'MdcPinNumber', 'CertificateNumber')
    empty_value_display = '-empty-'


admin.site.register(ExportData, ExportDataAdmin)