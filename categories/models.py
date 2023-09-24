from django.db import models

# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=200, unique=True, blank=False)
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "Categories"
        ordering = ("-id",)
