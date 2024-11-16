from django.shortcuts import render
from django.views import generic
from .models import Meals, FOOD_TYPE


## Display menu as a list view class
class MealsList(generic.ListView):
    queryset = Meals.objects.order_by("-date_created")  ## Connects values in model database to the view
    template_name = "index.html"  ## connects view to html

    ## Usinng context manager and jinja to get data on html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["types"] = FOOD_TYPE
        return context


class MealDetail(generic.DetailView):
    model = Meals
    template_name = "meal_detail.html"
