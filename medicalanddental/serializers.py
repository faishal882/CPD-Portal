from rest_framework import serializers
from .models import ExportData

class ExportSerializer(serializers.ModelSerializer):
 class Meta:
        model = ExportData
        fields = ('Name', 'CourseTitle', 'MdcPinNumber', 'CertificateNumber', 'DateOfCompletion', 'Type' )