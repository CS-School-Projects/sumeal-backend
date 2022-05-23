from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views import View
from .models import Meals, MealCategory
from .form import MealForm
# authentication of users is

# Create your views here.

class IndexView(View):
    template_name = 'index.html'
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)


class MealsView(View):
    template_name = 'meal.html'
    def get(self, request):
        meals = Meals.objects.all()
        context = {'meals':meals}
        return render(request, self.template_name, context)





class AddMealView(View):
    # meal = MealForm()
    def get(self, request):
        categories = MealCategory.objects.all()
        context={'categories':categories}
        return render(request, 'add-meal.html', context)

    def post(self, request):
        query = request.POST.get('category')
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully')
            return redirect('dashboard:meals')
        else:
            messages.error(request, form.errors)
            return redirect('dashboard:add-meals')



class UpdateMealView(View):
    meal = MealForm()
    def get(self, request, pk):
        item = Meals.objects.filter(id=pk).first()
        categories = MealCategory.objects.all()
        context={'item':item, 'categories':categories}
        return render(request, 'add-meal.html', context)

    def post(self, request, pk):
        item = Meals.objects.filter(id=pk).first()
        form = MealForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully')
            return redirect('dashboard:meals')
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

     

class DeleteMealView(View):
    def get(self, request, *args, **kwargs):
        return redirect('dashboard:meals')

    def post(self, request, *args, **kwargs):
        meal = Meals.objects.filter(id=request.POST.get('meal_id')).first()
        if meal:
            meal.delete()
            messages.success(request,'Meal Deleted Successfully')
        else:
            messages.error(request,'Meal Not Found')
        return HttpResponseRedirect(request.META.get('HTTP-REFERER'))



    
   

   


   