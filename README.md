# Udemy Django Full Stack Web Developer Course

Notes and exercises for the [Udemy Python and Django Full Stack Web Developer Bootcamp](https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp/) course.


# Basic Django Workflow: Commands to Start Project, Create and App, and Create a Simple View

**### NOTE: lecture 132 (last lecture of section 17) provides a great overview of all Django basics in sections 16 and 17, covering how to create a project, create an app within the project**
set up models/views/templates and wire the views up to URLs.

**Before step 1, need to activate conda env w/ Django**: `$ conda activate myDjangoEnv`

1. Create a project: `django-admin startproject ThrowAwayTest`. Note this will create files/folders like this: 

![Alt text](misc_images/django_project_initial_structure.png)

2. Go to the project directory: `cd ThrowAwayTest`
3. Create an app within the project: `python manage.py startapp basic_app`
4. Add `templates/` folder to root of project dir (HTML files w/ Django template tags go here)
5. Edit settings.py to let project know that the app exists by adding the app to INSTALLED_APPS:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'basic_app' # new app added here
]
```
6. Edit settings.py to specify the directory where templates are stored:
```python
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# ... #

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,], # NOTE: TEMPLATE_DIR added here!
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

7. Draft super basic HTML files under `templates/` starting w/ `index.html` and then maybe one other page like `other.html` (can add template tags later for data injection)
8. Create a new view by editing `views.py` within the app folder. Specifically, configure the HTML returned by a request like this:
```python

# Super simple, not used often

from django.http import HttpResponse
def index(request):
    return HttpResponse("<em>My Second Project</em>")


# typical approach using `render()` and providing a context dictionary where keys can be referenced using `{{ }}` in the template HTML files:
from django.shortcuts import render

def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'basic_app/index.html', context_dict)

```
9. Link the new view to a url by editing the main `urls.py` within the project sub-folder. Specifically, add something like this: 
```python
from basic_app import views # don't forget to import views from app subfolder we created
from django.urls import path, re_path, include


urlpatterns = [
    path('', views.index, name='index'), # so we can go to https://127.0.0.1:8000/admin/ to access index.html
    path('admin/', admin.site.urls), # so we can go to https://127.0.0.1:8000/admin/ to access built-in Django admin UI
    re_path('^basic_app/', include('basic_app.urls')),
]
```
10. Now add another `urls.py` file to the app subfolder (e.g., `basic_app`) and specify paths:
```python
from basic_app import views # don't forget to import views from app subfolder we created
from django.urls import path, re_path, 
urlpatterns = [
    re_path(r'^other/$', views.other, name='other') # so we can go to https://127.0.0.1:8000/basic_app/other/ to access built-in Django admin UI
]
```
11. Run the server locally to test it out: `python manage.py runserver`
12. Copy local host address into address bar to see the site


**NOTE:** the above workflow is not ideal. It's best practice to put another urls.py file inside of each individual app, then refer to that
file in your project folder using `django.conf.urls.include`. For an example, see `14-Django_Level_One/first_project`. Within this folder,
the first_project subfolder contains a `urls.py` file that references the `urls.py` file found in `first_app/urls.py`. This approach creates 
modularity, making it simpler to plug your apps into different Django projects.

## Getting Started Build a Website with Django
I think this is a pretty good workflow:

1. First complete steps 1-6 above to get the basic setup
1. 

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
      ```python
      import os 
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

      import django
      django.setup()
      ``` 
    - run script: `python populate_models.py`
7. Now need to add the following to `admin.py` to register the model w/ admin so that we can view the data we add in the admin:
    ```python
    from basic_app.models import ModelName

    # Register your models here.
    admin.site.register(ModelName)
    ```
8. `python manage.py createsuperuser` — create super user from command line (I used username = jordan, email=my personal email, password = 1234 for for my sample app)
9. Now can run server on local host w/ `python manage.py runserver`, then go to `http://127.0.0.1:8000/admin` and enter credentials to log in, where one can view the data 
   and even add/delete data to the models using the admin UI that comes built in w/ Django