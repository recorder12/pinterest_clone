from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'

    # get form data
    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # commit=False : not store to DB
        temp_profile.user = self.request.user  # add requested user as user data
        temp_profile.save()  # finally save to DB
        return super().form_valid(form)  # super() allows to access methods of the base class

    # custom redirect url
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    template_name = 'profileapp/update.html'

    # adjust get_success_url with pk
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})