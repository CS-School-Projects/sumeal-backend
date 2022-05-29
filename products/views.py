from dataclasses import field
from django.views import View
from pdb import post_mortem
from pyexpat import model
from statistics import mode
from tkinter.tix import Tree
from django import views
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from requests import post
from products.models import Category
from products.mxins import CreateUpdateMixin, DeletionMixin
from products.forms import ProductForm,CategoryForm
from products.models import Product
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.html import strip_tags
from .forms import CategoryForm


class ProductsView(View):
    template_name = "products/products.html"

    @method_decorator(login_required(login_url="accounts:login"))
    def get(self, request):
        products = Product.objects.all()
        context = {
            "products": products,
        }
        return render(request, self.template_name, context)


class ChangeProductView(CreateUpdateMixin):
    template_name = "products/edit_product.html"
    form_class = ProductForm
    object_id_field = "product_id"
    model_class = Product
    object_name = "product"

    @method_decorator(login_required(login_url="accounts:login"))
    def get(self, request):
        object_id = request.GET.get(self.object_id_field)
        obj = self.model_class.objects.filter(id=object_id).first()
        categories = Category.objects.all()
        context = {
            self.object_name: obj,
            "categories": categories,
        }
        return render(request, self.template_name, context)

    @method_decorator(login_required(login_url="accounts:login"))
    def post(self, request):
        object_id = request.POST.get(self.object_id_field) or -1
        obj = self.model_class.objects.filter(id=object_id).first()
        form = self.form_class(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("products:products")
        else:
            for field, error in form.errors.items():
                message = f"{field.title()}: {strip_tags(error)}"
                break
            context = {k: v for k, v in request.POST.items()}
            messages.warning(request, message)
            return render(request, self.template_name, context)


class DeleteProductView(DeletionMixin):
    object_id_field = "product_id"
    model_class = Product

def CategoryView(request):
    submitted = False
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()   
            return HttpResponseRedirect(request.path_info)
    else:

        form = CategoryForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request,'products/category.html',{'form':form , 'submitted':submitted})