from django import forms 
from django.contrib.auth.models import User 
from basic_app.models import UserProfileInfo

# this code serves to collect the info from the registration form

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password') # just include a subset of the fields in User


# NOTE: form class should typically be the name of the corresponding model (UserProfileInfo in this case)
# Plus "Form". Don't want to give form and model class the same name
class UserProfileInfoForm(forms.ModelForm): 
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')