from django.shortcuts import render
from django.views.generic import CreateView
from .models import Category
from .forms import addcategoryForm,updatecategoryForm
# Create your views here.

def index(request):
    return render(request,'index.html')


class addcategory(CreateView):
    model = Category
    form_class = addcategoryForm
    template_name = 'addcategory.html'

class updatecategory(CreateView):
    model = Category
    form_class = updatecategoryForm
    template_name = 'updateCategory.html'
