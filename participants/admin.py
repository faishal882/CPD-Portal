from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import Profile

class ProfileAdmin(ImportExportModelAdmin):
    list_display = [ 'name','hospital', 'profession', 'pin','mobile', 'gender' ]
    show_full_result_count = True
    empty_value_display = '-empty-'



admin.site.register(Profile, ProfileAdmin)
