from django import forms
from products.models import Category, Product


class CategoryFormReal(forms.ModelForm):
       name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Category Name"}))
       description = forms.CharField(widget=forms.Textarea(attrs={
        'rows' : 4,
        'class' : 'form-control',
        }))
       class Meta:
          model = Category
          fields = ['name','description']
       
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