from django import forms 
from django.contrib.auth.models import User 
from basic_app.models import UserProfileInfo

# this code serves to collect the info from the registration form

class UserProfileInfoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fiels = ('username', 'email', 'password') # just include a subset of the fields in User


class UserProfileInfo(forms.ModelForm):
    class Mera:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')