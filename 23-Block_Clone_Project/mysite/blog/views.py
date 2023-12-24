from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, 
                                  DetailView, CreateView, 
                                  UpdateView, DeleteView)
from blog.models import Post, Comment
from django.utils import timezone
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy

# analog of django.contrib.auth.decorators.login_require but for class-based views rather than function-based
from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.

class AboutView(TemplateView):
    """ template view for about page """

    template_name = 'about.html'


class PostList(ListView):
    """ view of list of posts """

    model = Post

    def get_query(self):
        """ 'python-ese' for SQL query """
        # NOTE: the '-' in '-published_date' specifies sorting in descending order
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') 

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin, CreateView):
    
    # need to restrict create post view to the super user
    ## so we set attributes for LoginRequiredMixin
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html' # redirect user to detail view
    form_class = PostForm

    model = Post 


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html' # redirect user to detail view
    form_class = PostForm

    model = Post 

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    # recall reverse_lazy() makes it so we don't go to success URL until we've actually deleted
    success_url = reverse_lazy('post_list') # defines where we go after deleting post


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_query_set(self):
        # drafts should have a null publication date, so we filter accordingly for this draft list view
        return Post.objects.filter(published_date__is_null=True).order_by('created_date')