from django.db import models
from users.models import CustomUser
import os
# Create your models here.


class Product(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200, default="", blank=False)
    image = models.ImageField()
