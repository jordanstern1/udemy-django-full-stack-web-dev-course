from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse # old django has resolve under contrib
from django.contrib.auth.decorators import login_required 

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


@login_required
def special(request):
    return HttpResponse('You are logged in—nice!')

@login_required # you have to have logged in before you can access this logout view that returns you to the home (index) page
def user_logout(request): # called user_logout to avoid collision with imported "logout"
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False 

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() # save to db
            user.set_password(user.password) # hashing password
            user.save() # save hashed password to db

            profile = profile_form.save(commit=False) # don't commit yet or may get errors w/ collisions trying to overwrite user
            profile.user = user # sets up one-to-one relationship as we set up in model.spy (user attribute of "profile" model needs to match user attribute of "user" model)

            # use request.FILES to access uploaded files
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # give the form so user can register
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request, 'basic_app/registration.html', {'user_form': user_form,
                                                           'profile_form': profile_form,
                                                           'registered': registered
                                                           })

            


def user_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username') # recall this matches name="username" from the login form in login.html
        password = request.POST.get('password')

        user = authenticate(username=username, password=password) # one line of code for authentication :)

        if user:
            if user.is_active:
                login(request=request, user=user)

                # NOTE: reverese allows you to reference the url in urls.py by name
                # (recall we had path('', views.index, name='index') in our main urls.py file)
                return HttpResponseRedirect(reverse('index')) 
            
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print(f"Username {username} and password {password}")
            return HttpResponse("Invalid login details supplied!")
    else: 
        # nothing submitted
        return render(request, 'basic_app/login.html', {})