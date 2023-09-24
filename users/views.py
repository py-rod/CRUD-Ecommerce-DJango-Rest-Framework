from django.shortcuts import render
from .models import CustomUser
from .serializer import RegisterUserSerializer, MyTokenObtainPairSerializer, UserSerializerGet, UserSerializerUpdateData, UserSerializerGetAll

from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@api_view(["POST"])
def signup(request):
    data = request.data
    serializer = RegisterUserSerializer(data=data)
    if serializer.is_valid():
        user = CustomUser.objects.create(
            username=data["username"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            password=make_password(data["password"]),

        )
        serializer = RegisterUserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Signin(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    serializer = UserSerializerGet(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user = CustomUser.objects.get(id=request.user.id)
    serializer = UserSerializerUpdateData(user, request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_all_users(request):
    user = CustomUser.objects.all()
    serializer = UserSerializerGetAll(user, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAdminUser])
def get_user_by_id_admin(request, pk):
    user = CustomUser.objects.get(id=pk)
    serializer = UserSerializerGet(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_user(request, pk):
    user = CustomUser.objects.get(id=pk)
    user.delete()
    return Response({"message": "The user has been delete"})
