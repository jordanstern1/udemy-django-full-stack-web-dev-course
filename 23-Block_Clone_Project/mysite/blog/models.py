from django.db import models
from django.utils import timezone 
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    """ class for blog posts """

    author = models.ForeignKey('auth.User') # author will be connected to superuser (assuming only superuser creates blog posts)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now() # set the publish date when the user hits the publish button
        self.save()
    
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self): # must be called get_absolute_url (django looks for this)
        """ After I create a post, take me to the post detail page for the post we just created """
        return reverse("post_detail", kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    """ class for comments on blog posts """
    
    post = models.ForeignKey('blog.Post', related_name='comments') # each comment is associated with a post
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())

    approved_comment = models.Boolean(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        """ after comment created, take us back to main home page (list view of all posts) """
        return reverse('post_list')

    def __str__(self):
        return self.text


