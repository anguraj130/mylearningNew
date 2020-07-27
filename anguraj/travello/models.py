from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class Contact(models.Model):
    mobile = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=100)


class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_pics')
    desc = models.TextField()