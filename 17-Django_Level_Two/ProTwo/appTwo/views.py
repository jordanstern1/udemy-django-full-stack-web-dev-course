from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User

def index(request):
    # return HttpResponse("<em>Home page</em>")
    return render(request, 'appTwo/index.html')

def help(request):
    context_dict = {'inserted_text': 'helpy help test'}
    return render(request, 'appTwo/help.html', context=context_dict)


def users(request):
    context_dict = {'users': User.objects.order_by('last_name')}
    return render(request, 'appTwo/users.html', context=context_dict)