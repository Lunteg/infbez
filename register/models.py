from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = None
    usr = models.CharField(max_length=255, unique=True)
    pwd = models.CharField(max_length=255)

    USERNAME_FIELD = 'usr'
    REQUIRED_FIELDS = []
