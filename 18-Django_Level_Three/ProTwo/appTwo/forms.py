from django import forms 
from django.core import validators 
from appTwo.models import User


class NewUserForm(forms.ModelForm):
    class Meta:
        # first_name = forms.CharField()
        # last_name = forms.CharField()
        # email = forms.EmailField()

        # note this should always be called model
        model = User
        fields = '__all__' # use all the fields

