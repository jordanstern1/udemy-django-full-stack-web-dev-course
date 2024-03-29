import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django 
django.setup()

# FAKE POPULATION SCRIPT
import random
from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker 

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    
    # NOTE: objects.get_or_create() uses Django's ORM to retrieve an object from the database that matches the given arguments, or create one if it doesn't exist
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0] # 0th element of tuple returned is a reference to the object created
    t.save() # don't forget to save
    return t 


def populate(N=5):
    
    for entry in range(N):
        # get topic for entry
        top = add_topic()

        # create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]



if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print('populating complete.')