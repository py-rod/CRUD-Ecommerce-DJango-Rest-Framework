from django.shortcuts import render
from rest_framework.permissions import IsAdminUser
from .models import Categories
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializer import CategoriesSerializer, CategorySerializerGetAll, CategorySerializerUpdate
# Create your views here.


@api_view(["POST"])
@permission_classes([IsAdminUser])
def create_category(request):
    data = request.data
    serializer = CategoriesSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_categories(request):
    categories = Categories.objects.all()
    serializer = CategorySerializerGetAll(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def update_category(request, pk):
    category = Categories.objects.get(id=pk)
    serializer = CategorySerializerUpdate(category, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_category(request, pk):
    category = Categories.objects.get(id=pk)
    category.delete()
    return Response({"message": "The category has been delete"})
