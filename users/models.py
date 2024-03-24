from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200, null=True)
    # phone =
    # date_of_birth =

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
