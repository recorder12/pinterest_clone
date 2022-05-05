# from django.contrib.auth.models import Profile
from django.http import HttpResponseForbidden
from profileapp.models import Profile

# custom decorator
def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk']) # user with pk
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated