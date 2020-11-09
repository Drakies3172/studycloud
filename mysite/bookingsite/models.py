from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.TextField(max_length=100)
    district = models.TextField(max_length=100)
    capacity = models.TextField(max_length=100)
    description = models.TextField(default="")
    image = models.ImageField(blank = True, null = True,upload_to='images/')
    def __str__(self):
        return self.name

class Customer(models.Model):
    people = models.TextField(max_length=100,default='')
    room = models.TextField(max_length=100,default='')
    checkinday = models.TextField(max_length=100,default='')
    checkoutday = models.TextField(max_length=100,default='')
    name = models.TextField(max_length=100,default='')
    id_number = models.TextField(max_length=100,default='')
    email = models.TextField(max_length=100,default='')
    phone = models.TextField(max_length=100,default='')
    current_address = models.TextField(max_length=100,default='')
    hotel_name = models.TextField(max_length=100,default='')
    def __str__(self):
        return self.name
   