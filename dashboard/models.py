from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse





class Review:
    pass


class Meal:
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length = 200, unique = True)
    categoryType = models.CharField(max_length = 150)
    categoryDescription = models.TextField(max_length = 400)
    categoryImage = models.ImageField(upload_to = 'images/categoryImages', null=True,blank=True)
    


    def __str__(self):
        return self.categoryName + '|' + self.categoryType

    # redirect
    def get_absolute_url(self):
        return reverse('dashboard:index')