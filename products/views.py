from django.shortcuts import render
from .serializer import ProductSerializerGet, ReviewSerializer, ProductSerializer, ProductSerializerupdate
from .models import Product, Review
from users.models import CustomUser

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
# Create your views here.


@api_view(["GET"])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializerGet(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_category_products(request, pk):
    products = Product.objects.filter(series__id=pk)
    serializer = ProductSerializerGet(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def top_products(request):
    products = Product.objects.filter(rating__gte=4).order_by("-rating")[0:5]
    serializer = ProductSerializerGet(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_product(request, category, pk):
    product = Product.objects.get(series__id=category, id=pk)
    serializer = ProductSerializerGet(product, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([IsAdminUser])
def create_product(request):
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def product_update(request, category, pk):
    product = Product.objects.get(series__id=category, id=pk)
    serializer = ProductSerializerupdate(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def product_delete(request, category, pk):
    try:
        product = Product.objects.get(series__id=category, id=pk)
    except Product.DoesNotExist:
        return Response({"error": "The product not exist"})
    else:
        product.delete()
        return Response({"message": "The product has been delete"})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_review(request, category, pk):
    user = request.user
    product = Product.objects.get(series__id=category, id=pk)
    data = request.data

    review_exist = product.review_set.filter(user=user).exists()
    if review_exist:
        return Response({"message": "The product already reviewed"})
    elif data["rating"] == 0:
        return Response({"message": "Please, select a raiting"})
    else:
        review = Review.objects.create(
            user=user,
            product=product,
            title=user.username,
            rating=data["rating"],
            comment=data["comment"],
        )
        reviews = product.review_set.all()
        product.num_reviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        product.rating = total / len(reviews)
        product.save()
        return Response({"message": "The comment and review added"})
