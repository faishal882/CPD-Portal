from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.CharField(max_length=220, null=True, blank=True)
    profession =  models.CharField(max_length=220, null=True, blank=True)
    pin = models.IntegerField(null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    gender = models.CharField(
        null=True,
        blank=True,  
        max_length = 20,
        choices = GENDER_CHOICES,
        default = 'Male'
       )

    
    class Meta:
        ordering = ['-id']

def user_did_save(sender, instance, created, *args, **kwargs):

    if created:
        Profile.objects.get_or_create(name=instance)


post_save.connect(user_did_save, sender=User)
