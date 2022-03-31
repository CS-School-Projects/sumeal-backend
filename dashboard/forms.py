from django import forms
from .models import Category


class addcategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('categoryName','categoryType','categoryDescription','categoryImage')

        widgets = {
            'categoryName' : forms.TextInput(attrs={'class': 'form-control'}),
            'categoryType' : forms.TextInput(attrs={'class':'form-control'}),
            'categoryDescription' : forms.Textarea(attrs={'class': 'form-control'}),
            # 'categoryImage' : forms.FileInput(attrs={'class': 'form-control'})
        }


class updatecategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('categoryName','categoryType','categoryDescription','categoryImage')

        widgets = {
            'categoryName' : forms.TextInput(attrs={'class': 'form-control'}),
            'categoryType' : forms.TextInput(attrs={'class':'form-control'}),
            'categoryDescription' : forms.Textarea(attrs={'class': 'form-control'}),
            # 'categoryImage' : forms.FileInput(attrs={'class': 'form-control'})
        }