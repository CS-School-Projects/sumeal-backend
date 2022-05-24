from django.views import View
from django.contrib.auth.decorators import login_required
from products.models import Category
from products.mxins import CreateUpdateMixin, DeletionMixin
from products.forms import ProductForm
from products.models import Product
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.utils.html import strip_tags


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
