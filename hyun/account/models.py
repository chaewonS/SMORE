from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    company_name = models.CharField(max_length=50)
    company_logo = models.ImageField(upload_to = "account/", blank = True, null=True)
    company_number = models.CharField(max_length=20,default='')
    company_location = models.TextField(default='')

    def __str__(self):
        return self.username


class UserPaper(models.Model):
    companyFK = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    papers = models.FileField(upload_to="files/",blank=True, null=True)