from django.urls import path
from . import views

urlpatterns = [
    path("", views.MealsList.as_view(), name="index"),
    path("details", views.MealDetail.as_view(), name="meal_detail")
]