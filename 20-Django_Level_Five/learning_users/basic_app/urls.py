from django.urls import path, re_path
from basic_app import views 

app_name = 'basic_app' # needed for relative URLs in templating

urlpatterns = [
    re_path('^$', views.register, name='register'),
]