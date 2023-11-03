from django.db import models

# Create your models here.
class contdb(models.Model):
    firstname=models.CharField(max_length=20,null=True,blank=True)
    lastname=models.CharField(max_length=30,null=True,blank=True)
    email=models.CharField(max_length=50,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
class regidb(models.Model):
    name=models.CharField(max_length=20,null=True,blank=True)
    mob=models.IntegerField(null=True,blank=True)
    email=models.CharField(max_length=20,null=True,blank=True)
    username=models.CharField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)
    re_password=models.CharField(max_length=20,null=True,blank=True)
class cartdb(models.Model):
    qty=models.IntegerField(null=True,blank=True)
    username=models.CharField(max_length=50,null=True,blank=True)
    productname=models.CharField(max_length=50,null=True,blank=True)
    des=models.CharField(max_length=200,null=True,blank=True)
    total_price=models.IntegerField(null=True,blank=True)

