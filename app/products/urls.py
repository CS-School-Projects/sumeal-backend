from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.ProductsView.as_view(), name='products'),
    path("change", views.ChangeProductView.as_view(), name='change_product'),
    path("delete", views.DeleteProductView.as_view(), name='delete_product'),
]
