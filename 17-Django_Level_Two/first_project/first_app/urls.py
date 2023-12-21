# NOTE: tutorial uses django.conf.urls.url(), but this was deprecated in Django 3.0, and is removed in Django 4.0+.
# we could use django.urls.path instead, but this doesn't use regex patterns, so we use re_path instead
from django.urls import re_path
from first_app import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
]