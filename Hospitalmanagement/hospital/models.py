from django.db import models

# Create your models here.

class p_signup(models.Model):
    pname=models.CharField(max_length=50)
    adrs=models.TextField()
    city=models.CharField(max_length=20)
    contact=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    pasword=models.CharField(max_length=50)

class book_apointment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    contact=models.BigIntegerField()
    a_date=models.DateField()
    department=models.CharField(max_length=20)    
    d_name=models.CharField(max_length=20)

class d_signup(models.Model):
    dname=models.CharField(max_length=50)
    department=models.CharField(max_length=30)
    city=models.CharField(max_length=20)
    contact=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    pasword=models.CharField(max_length=50)

class contact_us(models.Model):
    name=models.CharField(max_length=30)
    contact=models.BigIntegerField()
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=100)
