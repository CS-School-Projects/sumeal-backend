from django.urls import path
from . import views
from .views import addcategory

app_name = "dashboard"

urlpatterns = [
    # Routes for locations
    path('', views.index, name="index"),

    # Route for adding categories
        # path('addcategory', views.addcategory, name="addcategory"),
        path('addcategory/', addcategory.as_view(), name="addcategory"),

]