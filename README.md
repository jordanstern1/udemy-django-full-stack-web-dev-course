# Udemy Django Full Stack Web Developer Course

Notes and exercises for the [Udemy Python and Django Full Stack Web Developer Bootcamp](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/) course.


# Basic Django Workflow: Commands to Start Project, Create and App, and Create a Simple View

**### NOTE: lecture 132 (last lecture of section 17) provides a great overview of all Django basics in sections 16 and 17, covering how to create a project, create an app within the project**
set up models/views/templates and wire the views up to URLs.

**Before step 1, need to activate conda env w/ Django**: `$ conda activate myDjangoEnv`

1. Create a project: `django-admin startproject ThrowAwayTest`. Note this will create files/folders like this: 

![Alt text](misc_images/django_project_initial_structure.png)

2. Go to the project directory: `cd ThrowAwayTest`
3. Create an app within the project: `python manage.py startapp AppTwo`
4. Create a new view by editing `views.py` within the app folder. Specifically, configure the HTML returned by a request like this:
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("<em>My Second Project</em>")
```
5. Link the new view to a url by editing `urls.py` within the project sub-folder. Specifically, add something like this: 
```
from appTwo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
]
```

6. Edit settings.py to let project know that the app exists by adding the app to INSTALLED_APPS:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appTwo' # new app added here
]
```
7. Run the server locally to test it out: `python manage.py runserver`
8. Copy local host address into address bar to see the site


**NOTE:** the above workflow is not ideal. It's best practice to put another urls.py file inside of each individual app, then refer to that
file in your project folder using `django.conf.urls.include`. For an example, see `14-Django_Level_One/first_project`. Within this folder,
the first_project subfolder contains a `urls.py` file that references the `urls.py` file found in `first_app/urls.py`. This approach creates 
modularity, making it simpler to plug your apps into different Django projects.

## More Useful Django Commands
### Migration commands

Migration commands to use inside project folder after making changes to models.py:
1. `python manage.py migrate` — apply migrations
2. `python manage.py makemigrations app_name` — register changes to application
3. `python manage.py migrate` — run this again for some reason
4. Optionally run `python manage.py shell` — open shell to interact with database, then can test:
    - `from app_name.models import ModelName`
    - `m = ModelName(field1="blah", field2='foobar')` - to construct object w/ data
    - `m.save()` to save the data we added
    - `print(ModelName.objects.all())` to see that data was added
6. Can create script to with fake data like this:
    - add script to root of project called, say, `populate_models.py` and add code like [this](17-Django_Level_Two/first_project/populate_first_app.py). Don't forget
      to add this at the top of the script:
      ```
      import os 
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

      import django
      django.setup()
      ``` 
    - run script: `python populate_models.py`
7. Now need to add the following to `admin.py` to register the model w/ admin so that we can view the data we add in the admin:
    ```
    from appTwo.models import ModelName

    # Register your models here.
    admin.site.register(ModelName)
    ```
8. `python manage.py createsuperuser` — create super user from command line (I used username = jordan, email=my personal email, password = 1234 for for my sample app)
9. Now can run server on local host w/ `python manage.py runserver`, then go to `http://127.0.0.1:8000/admin` and enter credentials to log in, where one can view the data 
   and even add/delete data to the models using the admin UI that comes built in w/ Django