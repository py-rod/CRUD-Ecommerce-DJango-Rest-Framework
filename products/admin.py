from django.contrib import admin
from .models import Product, Review
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "series", "user")
    list_display_links = ("id", "title")
    list_filter = ("series", "user")
    list_per_page = 20
    search_fields = ("id", "title")
    ordering = ("-id",)
