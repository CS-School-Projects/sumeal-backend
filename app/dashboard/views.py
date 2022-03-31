from django.contrib import messages
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






# def addMeal(request):
    
#     meal = MealForm()

#     if request.method == 'POST':
#         meal  = MealForm(request.POST,request.FILES)
#         if meal.is_valid():
#             meal.save()
#             return redirect('meals')
     


#     context={'meal':meal}
#     return render(request, 'add-meal.html', context)

class AddMealView(View):
    meal = MealForm()
    def get(self, request):
        context={'meal':self.meal}
        return render(request, 'add-meal.html', context)

    def post(self, request):

        form = MealForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully')
            return redirect('dashboard:add-meals')
        else:
            messages.error(request, form.errors)
            return redirect('dashboard:meals')



class UpdateMealView(View):
    meal = MealForm()
    def get(self, request, pk):
        item = Meals.objects.filter(id=pk).first()
        context={'meal':self.meal,'item':item}
        return render(request, 'add-meal.html', context)

    def post(self, request, pk):

        item = Meals.objects.filter(id=pk).first()
        form = MealForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully')
            return redirect('dashboard:add-meals')
        else:
            messages.error(request, form.errors)
            return redirect('dashboard:meals')

     
def deleteMeal(request, pk):
    meal = Meals.objects.get(pk=pk)
    if request.method == 'POST':
        meal.delete()
        return redirect('account')   





    
   

   


   