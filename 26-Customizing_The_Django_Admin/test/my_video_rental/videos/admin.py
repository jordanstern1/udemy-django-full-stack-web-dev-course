from django.contrib import admin
from . import models

# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    # this will reorder fields in detail view for a Movie record in admin
    # rather than using default ordering which will match ordering of fields in our model definition
    fields = ['release_year', 'title', 'length'] 

    # now we can search by a field!
    search_fields = ['title', 'length'] 

    # now we can filter by fields
    list_filter = ['release_year', 'length', 'title']

    # now we have multiple columns in the list view for movies—seems useful!
    list_display = ['release_year', 'length', 'title']

admin.site.register(models.Customer)
admin.site.register(models.Movie, MovieAdmin)