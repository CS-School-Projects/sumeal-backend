from django.shortcuts import render
from django.views.generic import CreateView
from .models import Category
from .forms import addcategoryForm
# Create your views here.

def index(request):
    return render(request,'index.html')

# def addcategory(request):
#     return render(request,"")

class addcategory(CreateView):
    model = Category
    form_class = addcategoryForm
    template_name = 'addcategory.html'
    # fields = '__all__'