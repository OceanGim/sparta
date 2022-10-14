from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserModel(AbstractUser):
    UserModel=models.CharField(default="UserModel", max_length=100)