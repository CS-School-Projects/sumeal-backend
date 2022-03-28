from django.shortcuts import render,redirect
from django.views import View
from .models import Meals
from .form import MealForm

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






def addMeal(request):
    
    meal = MealForm()

    if request.method == 'POST':
        meal  = MealForm(request.POST,request.FILES)
        if meal.is_valid():
            meal.save()
            return redirect('meals')
     


    context={'meal':meal}
    return render(request, 'add-meal.html', context)


def updateMeal(request, pk):
    meal = Meals.objects.get(pk=pk)
    meal = MealForm()

    if request.method == 'POST':
        meal  = MealForm(request.POST,request.FILES, instance = meal)
        if meal.is_valid():
            meal.save()
            return redirect('meals')
     


    context={'meal':meal}
    return render(request, 'add-meal.html', context)
     
def deleteMeal(request, pk):
    meal = Meals.objects.get(pk=pk)
    if request.method == 'POST':
        meal.delete()
        return redirect('account')   





    
   

   


   