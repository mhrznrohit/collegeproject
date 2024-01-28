from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=150)
    price = models.FloatField()
    pieces = models.IntegerField()
    image = models.ImageField(upload_to='images')
    slug = models.SlugField(max_length=255, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    


   
class CartItems(models.Model):
    ORDER_STATUS = (
        ('Active', 'Active'),
        ('Delivered', 'Delivered')
    )
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    itemtitle=models.CharField(max_length=50,default='x')
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    ordered_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Active')
    delivery_date = models.DateField(default=timezone.now)
    location = models.CharField(max_length=150, default='Ktm')
    class Meta:
        verbose_name = 'Cart Item'
        verbose_name_plural = 'Cart Items'
    

   

   