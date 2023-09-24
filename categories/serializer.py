from rest_framework import serializers
from .models import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["title", "active"]


class CategorySerializerGetAll(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class CategorySerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["title", "active"]
