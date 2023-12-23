from django.urls import path, re_path 
from basic_app import views

# remember we need this so we can refer to relative URLs in templates like {% basic_app:index %}
app_name = 'basic_app' 

urlpatterns = [
    re_path(r'^$', views.SchoolListView.as_view(), name='list'),
    re_path(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail'), # pk = primary key
]