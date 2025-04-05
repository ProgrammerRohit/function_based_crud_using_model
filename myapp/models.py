from django.db import models

# Create your models here.
class UserDetails(models.Model):
    name = models.CharField(max_length=40, verbose_name="User Name")
    email = models.EmailField(max_length=100, verbose_name="User Email")
    passw = models.CharField(max_length=100, verbose_name="User Password")