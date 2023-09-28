from django.db import models
from users.models import CustomUser
import os
from categories.models import Categories
# Create your models here.


class Product(models.Model):

    def image_upload_to(self, instance):
        if instance:
            return os.path.join("Product_image", self.title, instance)
        return None

    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, default="", blank=False)
    image = models.ImageField(
        default="./Default/noproduct.jpg", upload_to=image_upload_to)
    brand = models.CharField(max_length=200, blank=True)
    series = models.ForeignKey(
        Categories, default="", blank=False, on_delete=models.SET_DEFAULT)
    description = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    num_reviews = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=False, blank=False)
    stock = models.IntegerField(blank=False, default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Products"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, blank=True)
    rating = models.IntegerField(blank=True, default=0)
    comment = models.TextField(blank=True)
    creted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating}"

    class Meta:
        verbose_name_plural = "Reviews"
