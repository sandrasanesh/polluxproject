from django.db import models

# Create your models here.
class catdb(models.Model):


    cname=models.CharField(max_length=50,null=True,blank=True)
    des=models.CharField(max_length=100,null=True,blank=True)
    cimg=models.ImageField(upload_to="profle_img",null=True,blank=True)
class productdb(models.Model):
    cname = models.CharField(max_length=50, null=True, blank=True)
    pname=models.CharField(max_length=20,null=True,blank=True)
    des=models.CharField(max_length=50,null=True,blank=True)
    pri=models.IntegerField(null=True,blank=True)
    pimg=models.ImageField(upload_to="product_img",null=True,blank=True)


