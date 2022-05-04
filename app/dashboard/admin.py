from django.contrib import admin

# Register your models here.
from dashboard.models import Meals,MealCategory

admin.site.register(Meals)
admin.site.register(MealCategory)
