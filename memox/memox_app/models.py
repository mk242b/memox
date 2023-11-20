from django.db import models

# Create your models here.
class Memo(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    memo = models.CharField()
    password = models.CharField(max_length=10,null=True)