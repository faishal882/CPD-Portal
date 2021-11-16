from import_export import resources
from .models import ExportData

class ExportResource(resources.ModelResource):
    class Meta:
        model = ExportData