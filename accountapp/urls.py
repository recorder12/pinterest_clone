from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world' ),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'), # CBV need class.as_view() syntax
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'), # pk : primary key (id)
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),# pk : primary key (id)
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete')  # pk : primary key (id)
]