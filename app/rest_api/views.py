from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from products.models import Category, Order, Product, Cart
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    UserSerializer,
    CreateUserSerializer,
    LoginUserSerializer,
    CartSerializer,
    OrderSerializer,
)

User = get_user_model()


# Create  API View for register
class RegisterAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
            "user":
            UserSerializer(user, context=self.get_serializer_context()).data,
            "token":
            token[1],
        })


# Create API View for Login
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        # print(user)
        if user:
            token = AuthToken.objects.create(user)
            return Response({
                "user": UserSerializer(user).data,
                "token": token[1]
            })
        else:
            return Response({"message": "Invalid credentials."})


# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LogoutAPI(generics.RetrieveAPIView):
    def post(self, request, *args, **kwargs):
        res = AuthToken.objects.filter(user=request.user).delete()
        return Response({"message": "Logged out successfully."})


class CategoryAPI(generics.GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, *args, **kwargs):
        categories = Category.objects.all().order_by("id")
        return Response(
            {"categories": self.serializer_class(categories, many=True).data})


class ProductAPI(generics.GenericAPIView):
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return Response({
            "products":
            self.serializer_class(products,
                                  context={
                                      "request": request
                                  },
                                  many=True).data
        })


class CartAPI(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrdersAPI(generics.ListAPIView):
    qs = Order.objects.all()
    serializer_class = OrderSerializer
