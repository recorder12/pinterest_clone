from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

# function based view
def hello_world(request):

    if request.method == "POST":

        # get data from name
        temp = request.POST.get('hello_world_input')

        # HelloWorld.objects.all().delete()

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else :
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


# class based view
class AccountCreateView(CreateView):
    model = User # default django user model
    form_class = UserCreationForm # default django form
    success_url = reverse_lazy('accountapp:hello_world') # reverse_lazy ~= reverse
    template_name = 'accountapp/create.html' # view template

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User  # default django user model
    form_class = AccountUpdateForm  # customized form
    success_url = reverse_lazy('accountapp:hello_world')  # reverse_lazy ~= reverse
    template_name = 'accountapp/update.html'  # view template