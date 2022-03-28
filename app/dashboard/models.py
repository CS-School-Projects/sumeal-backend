from re import T
import re
from django.db import models
import uuid


class Meals(models.Model):
    customer_name = models.CharField(max_length=200, null=True, blank=True)
    meal_type = models.CharField(max_length = 300, null=True, blank=True)
    meal_price = models.FloatField(null=True, blank=True)
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    created_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.meal_type
    

# class Review:
#     pass


# class Category:
#     pass
