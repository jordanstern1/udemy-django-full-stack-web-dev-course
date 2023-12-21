"""ProTwo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from appTwo import views

urlpatterns = [
    # When you include URL patterns from an app (appTwo in your case) in 
    # your project's main urls.py file using include('appTwo.urls'), Django effectively appends 
    # the patterns from appTwo/urls.py to the path specified in the main urls.py.
    
    # path('help/', views.help, name='help'),
    re_path(r'^help/.*', views.help, name='help'), # NOTE: use re_path() for regex matching, use path() for exact string matching
    path('', views.index, name='index'),
]
