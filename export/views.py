from django.http import HttpResponse
from .resource import ExportResource

def csv_export(request, *args, **kwargs):
    csv_resource = ExportResource()
    dataset = csv_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return response

def excel_export(request, *args, **kwargs):
    excel_resource = ExportResource()
    dataset = excel_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    return response
