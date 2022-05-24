from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.utils.html import strip_tags
from django.views import View


class CreateUpdateMixin(View):
    @method_decorator(login_required(login_url="accounts:login"))
    def get(self, request):
        object_id = request.GET.get(self.object_id_field)
        obj = self.model_class.objects.filter(id=object_id).first()
        context = {self.object_name: obj}
        return render(request, self.template_name, context)

    @method_decorator(login_required(login_url="accounts:login"))
    def post(self, request):
        object_id = request.POST.get(self.object_id_field) or -1
        obj = self.model_class.objects.filter(id=object_id).first()
        form = self.form_class(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("dashboard:index")
        else:
            for field, error in form.errors.items():
                message = f"{field.title()}: {strip_tags(error)}"
                break
            context = {k: v for k, v in request.POST.items()}
            messages.warning(request, message)
            return render(request, self.template_name, context)


class DeletionMixin(View):
    @method_decorator(login_required(login_url="accounts:login"))
    def get(self, request):
        return redirect("dashboard:index")

    @method_decorator(login_required(login_url="accounts:login"))
    def post(self, request):
        object_id = request.POST.get(self.object_id_field) or -1
        res = self.model_class.objects.filter(id=object_id).delete()
        if res and res[0]:
            messages.success(request, "Deleted successfully.")
        else:
            messages.info(request, "Item not found.")
        return redirect(request.META.get("HTTP_REFERER") or "dashboard:index")
