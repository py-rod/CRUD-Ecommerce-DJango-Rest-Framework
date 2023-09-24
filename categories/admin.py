from django.contrib import admin
from .models import Categories
# Register your models here.


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    list_filter = ("active", )
    list_per_page = 20
    search_fields = ("id", "title")
    ordering = ("-id",)
