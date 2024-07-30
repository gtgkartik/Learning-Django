from django.db import models


class Product (models.Model):  # this basically means we are creating a new class called Product that inherits from models.Model
    title = models.CharField(max_length=255)  #  CharField with a max length of 255
    description = models.TextField()  # TextField  # this is a field that is a TextField the maximum length is not required
    price = models.DecimalField(max_digits=8, decimal_places=2)  # tDecimalField with a max_digits of 6 and decimal_places of 2 example: 1234.56, these two arguments are required
    inventory = models.IntegerField()  #  IntegerField example: 1234 
    last_updated = models.DateTimeField(auto_now=True)  # DateTimeField with auto_now=True, this means that the field will be automatically set to now every time the object is saved
    
class Customer(models.Model):
    
    membership = [
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold')
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True) # EmailField, unique=True means that the value must be unique in the table
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True) # that is a DateField, null=True means that the value can be NULL in the table
    membership = models.CharField(max_length==1, choices = membership)
    

# By default django models will have primary key as id but if you want tyour own id then you can do it like this "sku = models.CharField(max_length=255, primary_key=True)"

class Order(models.Model):
    payment_status = [
        ('P', 'Pending'),
        ('C', 'Confirmed'),
        ('F', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=payment_status)
    
    
# here Address is a child and the parent is the Customer
class Address(models.Models):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=true) # OneToOneField with on_delete=models.CASCADE, this means that if the parent object is deleted, then the child object will also be deleted, the primary key has been set to true coz we want to make the customer as the primary key and it will be our one to one relationship