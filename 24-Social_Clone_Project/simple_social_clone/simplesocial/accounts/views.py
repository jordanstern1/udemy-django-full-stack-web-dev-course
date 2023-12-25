from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm # not instantiating class
    success_url = reverse_lazy('login') # lazily evaluate so doesn't execute until user has signed up
    template_name = 'accounts/signup.html'