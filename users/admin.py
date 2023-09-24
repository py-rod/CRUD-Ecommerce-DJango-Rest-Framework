from django.contrib import admin
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    list_display_links = ("id", "username", "email")
    list_per_page = 20
    search_fields = ("id", "username", "email")
    ordering = ("-id",)
