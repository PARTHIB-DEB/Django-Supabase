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