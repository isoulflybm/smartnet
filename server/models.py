from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 256)
    email = models.CharField(max_length = 64)
    phone = models.CharField(max_length = 32)
    password = models.CharField(max_length = 128)

    
