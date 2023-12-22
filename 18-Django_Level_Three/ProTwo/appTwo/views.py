from django.shortcuts import render
from django.http import HttpResponse
# from appTwo.models import User
from appTwo.forms import NewUserForm

def index(request):
    # return HttpResponse("<em>Home page</em>")
    return render(request, 'appTwo/index.html')

def help(request):
    context_dict = {'inserted_text': 'helpy help test'}
    return render(request, 'appTwo/help.html', context=context_dict)


def users(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if  form.is_valid():
        
            form.save(commit=True) # save the data inputted by the user

            return index(request) # this will return the rendering request of the home page
        else:
            print('ERROR: FORM INVALID')

    return render(request, 'appTwo/users.html', {'form': form})