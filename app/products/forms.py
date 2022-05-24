from django import forms
from products.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = [
            "id",
            "created_at",
            "updated_at",
        ]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [
            "id",
            "created_at",
            "updated_at",
        ]