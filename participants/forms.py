from django import forms
from .models import GENDER_CHOICES, Profile


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    hospital = forms.CharField(required=True)
    profession = forms.CharField(required=True)
    pin = forms.IntegerField(required=True)
    mobile = forms.IntegerField(required=True)
    gender = forms.ChoiceField(required=True, choices=GENDER_CHOICES)

    class Meta:
        model = Profile
        fields = ['first_name','last_name','hospital', 'profession', 'pin','mobile', 'gender']
