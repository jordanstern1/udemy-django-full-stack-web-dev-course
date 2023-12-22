from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

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

            


    return render