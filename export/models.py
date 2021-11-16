from typing import Type
from django.db import models


class ExportData(models.Model):
    Name = models.CharField('user-name', max_length=100)
    CourseTitle = models.CharField(max_length=10)
    MdcPinNumber = models.IntegerField(null=True, blank=True)
    CertificateNumber = models.IntegerField(null=True, blank=True)
    DateOfCompletion = models.DateField(blank=True, null=True)
    Type = models.CharField('Type', max_length=100)

    def __str__(self):
        return self.Name
