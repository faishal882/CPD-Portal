from django.shortcuts import redirect, render
from .forms import ProfileForm


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

