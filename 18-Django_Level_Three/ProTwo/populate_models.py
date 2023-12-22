import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()


from faker import Faker
from appTwo.models import User 

fake = Faker()

def add_user(first_name, last_name, email):
    
    u = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)[0]
    u.save()
    
    return u

def populate(N=10):
    
    for i in range(N):
        print(f'\t--> added user {i}')
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()
        u = add_user(fake_first_name, fake_last_name, fake_email)
    
    return
    


if __name__ == '__main__':
    print('populating fake users...')
    populate(20)
    print('done populating.')