from django import forms
from .models import Meals
from django.forms import ModelForm


class MealForm(ModelForm):
    class Meta:
        model = Meals
        fields =['customer_name', 'meal_type', 'meal_price']
        # change tags to checkboxes
        
    def __init__(self, *args, **kwargs):
        super(MealForm, self).__init__(*args, **kwargs)

    # YOU HAVE TO DO FOR EACH ATTRIBUTE, TO AVOID THAT STRESS, WRITE A FOR LOOP FOR THAT

        for name, field in self.fields.items():
             field.widget.attrs.update({'class':'input'})
