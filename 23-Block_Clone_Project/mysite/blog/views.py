from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, 
                                  DetailView, CreateView, 
                                  UpdateView, DeleteView)
from blog.models import Post, Comment
from django.utils import timezone
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# analog of django.contrib.auth.decorators.login_required but for class-based views rather than function-based
from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.

class AboutView(TemplateView):
    """ template view for about page """

    template_name = 'about.html'


class PostListView(ListView):
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
    

##################################################
## Comment views below
##################################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required # view can only be seen if logged in
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        # form has been filled in and submitted
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post # remember each comment is associated wth a post in our Comment model
            comment.save()
            return redirect('post_detail', pk=post.pk)
        
        else:
            # comment form hasn't been filled out yet
            form = CommentForm()
        
        return render(request, 'blog/comment_form.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment)
    comment.approve()

    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment)
    post_pk = comment.post.pk
    comment.delete()

    return redirect('post_detail', pk=post_pk)