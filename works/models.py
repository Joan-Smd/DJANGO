from django.db import models

# Create your models here.
class register(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    date = models.DateField(null=True)
    place = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    confirmpass = models.CharField(max_length=20)

class cusfeed(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    date = models.DateField(null=True)
    place = models.CharField(max_length=30)
    message = models.CharField(max_length=200)

class userbook(models.Model):
    email = models.EmailField(max_length=30)
    place = models.CharField(max_length=100)
    room = models.CharField(max_length=50)
    guest = models.IntegerField()
    date = models.DateField(null=True)
    checkin = models.DateField(null=True)
    checkout = models.DateField(null=True)
    note = models.CharField(max_length=200)
    payment = models.CharField(max_length=30)
    status = models.CharField(max_length=30)

class newadmin(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uname = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    password = models.CharField(max_length=30)

class addplaces(models.Model):
    place = models.CharField(max_length=30)

class payments(models.Model):
    cname = models.CharField(max_length=50)
    cnumber = models.CharField(max_length=16)
    expmonth = models.CharField(max_length=10)
    expyear = models.CharField(max_length=10)
    cvv = models.CharField(max_length=10)