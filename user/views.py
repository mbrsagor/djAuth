from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserCreationForm


class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('/accounts/login/')
    template_name = 'signup.html'
