from django.db import models
class Register(models.Model):
    Name=models.CharField(max_length=10)
    Place=models.CharField(max_length=10)
    Age=models.IntegerField()
    Email=models.EmailField()
    Password=models.CharField(max_length=10)
class Image(models.Model):
    ImageName=models.CharField(max_length=10)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Price=models.IntegerField()
    

