from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name
    
    def get_absolute_url (self):
        return reverse("basic_app:detail", kwargs={'pk': self.pk})
    
class Student(models.Model):

    # note no primary key is defined, but Django will automatically set an "id" primary key
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()

    # related_name allows me to then call school_detail.students.all in our school_detail.html
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name