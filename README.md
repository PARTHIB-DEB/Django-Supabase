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

![image](https://github.com/PARTHIB-DEB/testsupa/assets/103876861/80f58a0a-1dda-4a70-97db-0afd36e9ab83)

 -**Copy Everything from connnection-parameters and paste it inside the SETTINGS.PY of django-project**

 Here remind one thing , Django natively **supports Multi-Model Databases** 😄. Means , You are hosting some of your models in Database A and some on Database B where each model eventually will be converted into a SQL relational table. But for that , you have to mention the dict-name of the proper database inside the models. Look at the settings file - 

```bash
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
```

 

