from django.shortcuts import render


def index(request):
    template_name = "website/index.html"
    return render(request, template_name)