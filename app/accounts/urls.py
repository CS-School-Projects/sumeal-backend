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
from accounts.views import RegisterAPI, LoginAPI
from knox import views as knox_views

urlpatterns = [
    path("api/register/", RegisterAPI.as_view(), name="register"),
    path("api/login/", LoginAPI.as_view(), name="logout"),
    path("api/logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("api/logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
]
