from django.urls import path
from . import views


urlpatterns = [
    path("add/", views.add_order_item, name="add_order_item"),
    path("myorders/", views.get_my_orders, name="get_my_orders"),
    path("orders/", views.get_orders, name="get_orders"),
    path("pay/<pk>/", views.update_order_to_paid, name="paid_order"),
    path("deliver/<pk>/", views.update_order_to_delivered, name="delivered_order"),
]
