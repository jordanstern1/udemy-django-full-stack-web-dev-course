from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin, 
                                        PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic
from groups.models import Group, GroupMembers

# Create your views here.

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description') # only editable fields
    model = Group # connect to group model

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group