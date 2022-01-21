from django.db import models




class reg(models.Model):

    id = models.BigAutoField(primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=100)
    
class college_reg(models.Model):

    id = models.BigAutoField(primary_key=True)
    collegename=models.CharField(max_length=50)
    location=models.CharField(max_length=50,null=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=100)

   