from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_products, name="get_products"),
    path("category/<pk>/",
         views.get_category_products, name="category_products"),
    path("top/", views.top_products, name="top_products"),
    path("<category>/product/<pk>/",
         views.get_product, name="get_product"),

    #     CREATE PRODUCT
    path("create/", views.create_product, name="create_product"),
    #     UPDATE PRODUCT
    path("<category>/update/<pk>/", views.product_update, name="product_update"),
    #     DELETE PRODUCT
    path("<category>/delete/<pk>/", views.product_delete, name="product_delete"),
    #     CREATE COMMENT AND RATING PRODUCT
    path("<category>/reviews/<pk>/", views.create_review, name="create_review"),

]
