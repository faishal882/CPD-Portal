from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

COURSE_CHOICES = (
    ("A", "A"),
    ("B", "B"),
    ("C", "C"),
    ("D", "D"),
    ("E", "E"),
    ("F", "F"),
    ("G", "G"),
    ("H", "H"),
)


class MedicalDentalCouncil(models.Model):
    Username = models.CharField(max_length=15)
    CourseTitle = models.CharField(max_length=10)
    MdcPinNumber = models.IntegerField(null=True, blank=True)
    CertificateNumber = models.IntegerField(null=True, blank=True)
    DateOfCompletion = models.DateField(blank=True, null=True)
    EntryTime = models.TimeField(auto_now_add=True)
    EntryDate = models.DateField(auto_now_add=True)
    Course = models.CharField(
        null=True,
        blank=True,  
        max_length = 20,
        choices = COURSE_CHOICES,
        default="A"
       )

    def __str__(self):
        return self.Username

