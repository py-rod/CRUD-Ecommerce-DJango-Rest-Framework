from rest_framework import serializers
from .models import Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["user", "title", "image", "brand", "series",
                  "description", "rating", "num_reviews", "price", "stock"]


class ProductSerializerGet(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

    def get_reviews(self, obj):
        review = obj.review_set.all()
        serializer = ReviewSerializer(review, many=True)
        return serializer.data


class ProductSerializerupdate(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["user", "title", "image", "brand", "series",
                  "description", "rating", "num_reviews", "price", "stock"]
