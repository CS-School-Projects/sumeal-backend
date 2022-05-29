"""sumeal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


urlpatterns = [
    path("register/", views.RegisterAPI.as_view(), name="register"),
    path("user/", views.UserAPI.as_view(), name="user"),
    path("login/", views.LoginAPI.as_view(), name="login"),
    path("logout/", views.LogoutAPI.as_view(), name="logout"),
    path("category/", views.CategoryAPI.as_view(), name="category"),
    path("products/", views.ProductAPI.as_view(), name="products"),
    path("cart/", views.CartAPI.as_view(), name="cart"),
    path("orders/", views.OrdersAPI.as_view(), name="orders"),
]
