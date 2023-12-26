from django.contrib import admin
from . import models

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    # this will reorder fields in detail view for a Movie record in admin
    # rather than using default ordering which will match ordering of fields in our model definition
    fields = ['release_year', 'title', 'length'] 

admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)