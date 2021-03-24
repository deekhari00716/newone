from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
    id = models. AutoField(primary_key=True)
    fname = models.CharField(max_length=30,default='SOME STRING')
    lname = models.CharField(max_length=30,default='SOME STRING')
    email = models.CharField(max_length=30,null=True)
    password = models.CharField(max_length=30,null=True)
    repassword = models.CharField(max_length=30,null=True)
