from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    company_representative = models.CharField(max_length=6)
    company_name = models.CharField(max_length=50)
    company_number = models.CharField(max_length=10)
    company_email = models.EmailField(max_length=128)