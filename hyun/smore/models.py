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

class ItemImage(models.Model):
    itemFK = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="images/",blank=True, null=True)

class ExperRec(models.Model):
    exper_title = models.CharField(max_length=200)
    exper_body = models.TextField()
    exper_period = models.CharField(max_length=100)
    exper_pub_date = models.DateTimeField()
    exper_image = models.ImageField(blank=True, null=True)
    exper_author = models.ForeignKey('account.User', on_delete= models.CASCADE)

    def __str__(self):
        return self.exper_title