from django.db import models
from django.utils import timezone

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey('account.User', on_delete= models.CASCADE)
    
    def __str__(self):
        return self.item_name