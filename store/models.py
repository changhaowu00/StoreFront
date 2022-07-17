import email
from django.db import models
from django.forms import model_to_dict

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_updeate = models.DateTimeField(auto_now_add=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
