from django.urls import path, re_path 
from basic_app import views

# remember we need this so we can refer to relative URLs in templates like {% basic_app:index %}
app_name = 'basic_app' 

urlpatterns = [
    re_path(r'^$', views.SchoolListView.as_view(), name='list'),

    # NOTE:  pk = primary key, the regex uses a capture group to assign the key to a name called 'pk'
    ## Longer explanation:
    # Named Capture Groups ((?P<name>pattern)): The syntax (?P<name>pattern) is used for named capture groups.
    # Here, ?P<name> defines the name of the group and pattern is what the group matches. In your example, 
    # (?P<pk>\d+) defines a named capture group called pk that matches one or more digits. This is specific 
    #  to Python's regular expression syntax and is very useful in Django for capturing parts of the
    # URL and passing them as keyword arguments to views.
    re_path(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'), 
    re_path(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
    re_path(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    re_path(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
]