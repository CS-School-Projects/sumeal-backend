from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    # Routes for locations
    path('', views.IndexView.as_view(), name='index'),
    path('meals/', views.MealsView.as_view(), name='meals'),
    path('add-meals/', views.AddMealView.as_view(), name='add-meals'),
    path('update-meals/<str:pk>/', views.UpdateMealView.as_view(), name='update-meals'),
]