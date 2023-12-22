from django.db import models
from django.contrib.auth.models import User # built-in Django User model

# Create your models here.

class UserProfileInfo(models.Model):
    # default user doesn't have this attribute, so here we can extend the User class 
    # (don't use inheritance; can cause problems)
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE # now required in later version of Django
                                ) 

    # additional attributes added to User
    portfolio_site = models.URLField(blank=True)

    # blank = True so user isn't requires
    profile_pic = models.ImageField(upload_to='profile_pics', # folder where pics will be uploaded
                                    blank=True # so user isn't required to upload a pic
                                    ) 

    def ___str__(self):
        return self.user.username