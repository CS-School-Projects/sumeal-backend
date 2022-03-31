from re import T
import re
from django.db import models
import uuid


# class MealCategory(models.Model):
#     title = models.CharField(max_length=200)

#     def __str__(self):
#         return self.title

class Meals(models.Model):
    customer_name = models.CharField(max_length=200, null=True, blank=True)
    meal_type = models.CharField(max_length = 300, null=True, blank=True)
    meal_price = models.FloatField(null=True, blank=True)
    # meal_category = models.ForeignKey(MealCategory, on_delete=models.CASCADE)
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    created_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.meal_type
    