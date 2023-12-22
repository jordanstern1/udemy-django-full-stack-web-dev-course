from django.urls import path, re_path
from basic_app import views 


# TEMPLATE TAGGING
app_name = 'basic_app' # important to set up the app_name so we can reference it in our templates (see relative_url_templates.html)

urlpatterns = [
    re_path(r'^relative/$', views.relative, name='relative'),
    re_path(r'^other/$', views.other, name='other')
]