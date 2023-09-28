from django.contrib import admin
from . models import Order, OrderItem, ShippingAddress
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "payment_method", "created")
    list_display_links = ("id", "user", "payment_method")
    list_filter = ("payment_method",)
    list_per_page = 20
    search_fields = ("id", "user", "created")
    ordering = ("-id",)


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("id", "product",  "title", "qty", "price")
    list_display_links = ("id", "product",  "title")
    list_filter = ("order", )
    list_per_page = 20
    search_fields = ("id", "product", "order")
    ordering = ("-id",)


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ("id", "order", "address", "city", "postal_code", "country")
    list_display_links = ("id", "order", "address")
    list_filter = ("order", "city", "country")
    list_per_page = 20
    search_fields = ("id", "address",
                     "city", "postal_code", "country")
