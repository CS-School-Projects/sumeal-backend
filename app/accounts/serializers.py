from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        extra_kwargs = {"password": {"write_only": True}}

        def create(self, validated_data):
            user = User(
                email=validated_data["email"],
                username=validated_data["username"],
            )
            user.set_password(validated_data["password"])
            user.save()
            return user
