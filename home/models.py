from django.db import models

# Create your models here.
class Detail(models.Model):
    first_name = models.CharField(max_length=122)
    last_name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12 , null=True)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)
    