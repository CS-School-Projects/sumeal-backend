from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, CreateUserSerializer,LoginUserSerializer
from django.contrib.auth import authenticate



# Create  API View for register
class RegisterAPI(generics.GenericAPIView):
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token[1]
        })


#Create API View for Login
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        #print(username, password)
        user = authenticate(request, username=username, password=password)
        #print(user)
        if user:
            token = AuthToken.objects.create(user)
            return Response({
                "user": UserSerializer(user).data,
                "token": token[1]
            })
        else:
            return Response({
                "message":"Invalid credentials."
            })

# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class LogoutAPI(generics.RetrieveAPIView):
    def post(self, request, *args, **kwargs):
        res = AuthToken.objects.filter(user=request.user).delete()
        return Response({
            "message":"Logged out successfully."
        })

