from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, 
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
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


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')  # define fields user can create (a security measure)
    model = models.School

class SchoolUpdateView(UpdateView):
    # note location is excluded from list of updatable fields
    # so user cannot update location (should be fixed for a school)
    fields = ('name', 'principal') 
    
    model = models.School 

class SchoolDeleteView(DeleteView):
    
    fields = ('name', 'principal', 'location')
    model = models.School

    # reverse_lazy uses lazy evaluation
    # only evaluates when it'
    success_url = reverse_lazy("basic_app:list")


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
