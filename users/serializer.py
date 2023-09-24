from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "password"]


class UserSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name",
                  "last_name", "email", "image", "description"]


class UserSerializerUpdateData(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name",
                  "last_name", "description", "image"]


class UserSerializerGetAll(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["email"] = user.email
        token["image"] = user.image.url
        token["is_staff"] = user.is_staff

        return token
