from django.db import models
from django.utils.text import slugify 
import misaka 
from django.contrib.auth import get_user_model # returns currently active user model
from django.urls import reverse

User = get_user_model()
from django import template
register = template.Library()

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)

    # NOTE: 
    # A URL slug is a readable, SEO-friendly segment of a URL that explains the page's content, 
    # typically replacing spaces with hyphens and avoiding special characters.
    slug = models.SlugField(allow_unicode=True, unique=True)
    
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ['name']

class GroupMembers(models.Model):
    group = models.ForeignKey(Group, related_name='memberships')
    user = models.ForeignKey(User, related_name='user_groups')
    
    def __str__(self):
        self.user.username

    class Meta:
        unique_together = ('group', 'user') # combination has to be unique