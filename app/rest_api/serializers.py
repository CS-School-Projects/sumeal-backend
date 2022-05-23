from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from products.models import Category, Order, Product, Cart

User = get_user_model()


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


# Register Serializer for creating new user
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user


# Login Serializer for loggin in  a user
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, **data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid Details.")


# Serializers for Products,Category and Cart
class ProductSerializer(serializers.ModelSerializer):
    # Get the image url by serializing the 'ImageField'
    image = serializers.ImageField(
        max_length=None, use_url=True, allow_null=True, required=False
    )

    class Meta:
        model = Product
        fields = ["id", "category", "name", "price", "description", "image"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        # Model to be serialized
        model = Category
        # fields to be serialized
        fields = ["name", "description"]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user", "item", "quantity", "created_at", "updated_at"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        # Model to be serialized
        model = Order
        # Fields to be serialized
        fields = "__all__"
