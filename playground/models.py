from django.db import models


class Product (models.Model):  # this basically means we are creating a new class called Product that inherits from models.Model
    title = models.CharField(max_length=255)  #  CharField with a max length of 255
    description = models.TextField()  # TextField  # this is a field that is a TextField the maximum length is not required
    price = models.DecimalField(max_digits=8, decimal_places=2)  # tDecimalField with a max_digits of 6 and decimal_places of 2 example: 1234.56, these two arguments are required
    inventory = models.IntegerField()  #  IntegerField example: 1234 
    last_updated = models.DateTimeField(auto_now=True)  # DateTimeField with auto_now=True, this means that the field will be automatically set to now every time the object is saved
    
class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) # EmailField, unique=True means that the value must be unique in the table
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True) # that is a DateField, null=True means that the value can be NULL in the table
    

# By default django models will have primary key as id but if you want tyour own id then you can do it like this "sku = models.CharField(max_length=255, primary_key=True)"