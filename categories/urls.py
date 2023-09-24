from django.urls import path
from . import views


urlpatterns = [
    path("create/", views.create_category, name="create_category"),
    path("", views.get_all_categories, name="get_all_categories"),
    path("update/<pk>/", views.update_category, name="update_category"),
    path("delete/<pk>/", views.delete_category, name="delete_category")
]
