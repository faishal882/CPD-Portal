from import_export import resources
from .models import MedicalDentalCouncil

class MedicalExportResources(resources.ModelResource):
    class Meta:
        model = MedicalDentalCouncil
        fields = ('Username__username','CourseTitle', 'MdcPinNumber', 'CertificateNumber', 'DateOfCompletion', 'Course', 'EntryTime', 'EntryDate')