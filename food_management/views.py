from django.shortcuts import render
from django.views import generic
from .models import Meals


## Display menu as a list view class
class MealsList(generic.ListView):
    queryset = Meals.objects.order_by("-date_created")  ## Connects values in model database to the view
    template_name = "index.html"  ## connects view to html

    ## Usinng context manager and jinja to get data on html
    def get_context_data(self): ## Use this exact method name to overwrite the Listviews original method
        context = {"meals":"Pizza", "Ingredients":["Pizza Bread", "Pizza Sauce"]}  ## Context needs to be a dictionary
        return context


class MealDetail(generic.DetailView):
    model = Meals
    template_name = "meal_detail.html"
