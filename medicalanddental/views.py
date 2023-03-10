import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .resources import MedicalExportResources
from tablib import Dataset

@login_required(login_url='/auth/login/')
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html")

@login_required(login_url='/auth/login/')
def portal_view(request, *args, **kwargs):
    return render(request, "pages/portal.html")  

@login_required(login_url='/auth/login/')
def participants_view(request, *args, **kwargs):
    return render(request, "pages/participants.html")  

@login_required(login_url='/auth/login/')
def history_view(request, *args, **kwargs):
    return render(request, "pages/history.html")  


def csv_export(request, *args, **kwargs):
    csv_resource = MedicalExportResources()
    dataset = csv_resource.export()
    response = HttpResponse(dataset.csv, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data-export.csv"'
    return response

def excel_export(request, *args, **kwargs):
    excel_resource = MedicalExportResources()
    dataset = excel_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="MedicalCouncil-{datetime.datetime.today()}.xls"'
    return response


def excel_upload(request):
    if request.method == 'POST':
        person_resource = MedicalExportResources()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read())
        
        result = person_resource.import_data(dataset, dry_run=True)  # Test the data import
        print(result.has_errors())
        print("HHEhhhh")
        if not result.has_errors():
            print("working......")
            person_resource.import_data(dataset, dry_run=False) # Actually import now     

    return HttpResponseRedirect('/medical/portal/')