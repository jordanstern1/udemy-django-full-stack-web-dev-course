from django.shortcuts import render
from . import forms # or from basicapp import forms

# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()
    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid(): # form.is_valid() is generic validation of things like email, will do custom validation later
            # just printing to illustrate we can grab form data
            print()
            print('validation success!')
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])
            print()

    return render(request, 'basicapp/form_page.html', {'form': form})