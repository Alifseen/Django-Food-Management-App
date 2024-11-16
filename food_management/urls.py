from django.urls import path
from . import views

urlpatterns = [
    path("", views.MealsList.as_view(), name="index"),
    path("details/<int:pk>", views.MealDetail.as_view(), name="meal_detail")  ## added a dynamic placed for primarkey for whatever item is clicked
]