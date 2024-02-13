# Django-Supabase Starter Template 🐍 ⚡ 
This is a basic starter template for connecting **Django** with the firebase-alternative (they claim 😅) - **Supabase**. Let's see the steps -

## Steps 📋
### 1. Connect with Postgresql locally

Needs No introduction. Just Follow the tutorial below -

(Install the **requirements.txt** in this step)

https://github.com/PARTHIB-DEB/Manual-DJ-Postgres-Integration

### 2. Connect with Supabase
Before discussing about the steps , let us know what is Supabase - It's just a very common Postgres Instance along with some more DAAS (Database As A Feature) features like Dashboard to navigate , Cloud Storage. You have seen these type of things in Firebase , Appwrite . But they are built on the top of Nosql Database . Supabase does the same keeping a popular SQL db in center . Seems Interesting right ? 🌝 , let's discuss the steps now
_(Make sure you have done step-1 properly . That means till know you have a proper django project-app architecture , connected to a postgres instance locally)_


 -**Create a Supabase Account ➡️ Create one Organization ➡️ Create one project (Under the Organization)**

 _(It should look like this, Here **parthib** is Organization , **testsupa** is the Project)_


 ![image](https://github.com/PARTHIB-DEB/testsupa/assets/103876861/1ffc3063-cad0-47ed-8495-be258b25b7a9)

 -**Get your database connection's SSL certificate**

![image](https://github.com/PARTHIB-DEB/testsupa/assets/103876861/79b66d84-7266-40f2-be29-9b561954cf8d)

 
 -**Then Go the /yourReferenceNo/settings/database Url, it will be look like this**

![image](https://github.com/PARTHIB-DEB/testsupa/assets/103876861/9b9aa7d9-d458-404d-b630-12d26befcdfb)


 -**Copy Everything from connnection-parameters and paste it inside the SETTINGS.PY of django-project**

 Here remind one thing , Django natively **supports Multi-Model Databases** 😄. Means , You are hosting some of your models in Database A and some on Database B where each model eventually will be converted into a SQL relational table. But for that , you have to mention the dict-name of the proper database inside the models. Look at the settings file - 

```bash
 # Settings.py

  import os
from dotenv import load_dotenv # For keeping all of your personal supabase information private

load_dotenv()
pw = os.getenv("SUPABASE_PASSWORD")
host = os.getenv("SUPABASE_HOST")
user =  os.getenv("SUPABASE_USERNAME")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testsupa',
        'USER': 'testsupa',
        'PASSWORD': 'testsupa',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    },
    'remote':{
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': user,
        'PASSWORD': pw, 
        'HOST': host,
        'PORT': '5432',
        'CERT' : 'PROJ.prod-ca-2021.crt' # The SSL certificate , store it inside the PROJECT folder
    }
}
DATABASE_ROUTERS = ['PROJ.routers.CustomRouter']

--------------------------------------------------------------------------------------------------------------

# APP/models.py

from django.db import models

# Create your models here.

class Local(models.Model):                  # the class where your local data is saved
    _DATABASE = 'default'

    name = models.CharField(max_length=50)
    data = models.JSONField()
    
class Remote(models.Model):                 # the class for the remote data
    _DATABASE = 'remote'
    
    name = models.CharField(max_length=20)
    data = models.JSONField()

---------------------------------------------------------------------------------------------------------------

# PROJECT/routers.py

class CustomRouter(object):

    def db_for_read(self, model, **hints):
        return getattr(model, "_DATABASE", "default")

    def db_for_write(self, model, **hints):
        return getattr(model, "_DATABASE", "default")

    def allow_relation(self, obj1, obj2, **hints):
        """
        Relations between objects are allowed if both objects are
        in the master/slave pool.
        """
        db_list = ('default', 'remote')
        return obj1._state.db in db_list and obj2._state.db in db_list

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True
```
 -**In the code , You can see there is one variable DATABASE_ROUTERS , which is basically points to the routing function of CustomRouter - Used to Route between two models where one model is in Local Postgres and other one is in Remote Supabase**

 -**Now run the two commands**
```bash
 python manage.py migrate --database=remote


 python manage.py migrate --database=default

```
Now Navigate to your **Supabase** Account to see the **remote** database and navigate to your **local postgres instance** via psql to check the **local** instance. 

 

