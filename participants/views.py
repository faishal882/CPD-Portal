from django.shortcuts import redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from participants.models import Profile

from .forms import ProfileForm
from .serializers import ProfileSerializer

@login_required(login_url='/auth/login/')
def profile_update_view(request, *args, **kwargs):
    if not request.user.is_authenticated:  
        return redirect("/auth/login?next=/participants/update")
    user = request.user
    my_profile = user.profile
    form = ProfileForm(request.POST or None, instance=my_profile)
    print(form.non_field_errors)
    if form.is_valid():
        profile_obj = form.save(commit=False)
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        profile_obj.save()
        return redirect("/medical/participants/")
  
    return render(request, "pages/profile.html",  {'form':form})


# API FOR FETCHING PARTCIPANTS DATA
@api_view(['GET'])
def profile_api_view(request, *args, **kwargs):
    qs = Profile.objects.all()[:6]
    serializer = ProfileSerializer(qs, many=True)
    return Response(serializer.data, status=200)

