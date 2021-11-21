from django.http import HttpResponse
from django.shortcuts import render
from .resource import ExportResource
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ExportData
from .serializers import ExportSerializer

def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html")

def portal_view(request, *args, **kwargs):
    return render(request, "pages/portal.html")  

def login_view(request, *args, **kwargs):
    return render(request, "users/login.html")  


def register_user_view(request, *args, **kwargs):
    return render(request, "users/register_user.html")  

def csv_export(request, *args, **kwargs):
    csv_resource = ExportResource()
    dataset = csv_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data-export.csv"'
    return response

def excel_export(request, *args, **kwargs):
    excel_resource = ExportResource()
    dataset = excel_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data-export.xls"'
    return response




    