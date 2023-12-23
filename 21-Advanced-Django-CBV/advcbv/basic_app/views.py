from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from basic_app import models

# Create your views here.

class SchoolListView(ListView):
    """ use ListView  to pack all the objects into a list called 'schools' instead
    of having to put call model.objects.all or whatever
    """
    
    # name of list of schools will be school_list by default (lowercase model name + _list)
    # but we can set a custom name using context_object_name
    context_object_name = 'schools'

    model = models.School # now we have a list of all the records in the model 

class SchoolDetailView(DetailView):
    
    # name of detail viw of schools will be schools by default (lowercase model name)
    # but we can set a custom name using context_object_name
    context_object_name = 'school_detail'
    model = models.School 
    template_name = 'basic_app/school_detail.html'


## basic example with injection
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

## Super basic example
from django.http import HttpResponse
class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS BASED VIEWS ARE COOL!")
