from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>Home page</em>")

def help(request):
    context_dict = {'inserted_text': 'helpy help test'}
    return render(request, 'appTwo/help.html', context=context_dict)