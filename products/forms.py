from dataclasses import fields
from tkinter import Widget
from unicodedata import category
from django import forms
from products.models import Category, Product
from django.forms import ModelForm

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name','description')
        CategoryName = forms.CharField()
        Description = forms.CharField(widget=forms.Textarea,)
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

# class CategoryFormReal(forms.Form):
#     CategoryName = forms.CharField()
#     Description = forms.CharField(widget=forms.Textarea)