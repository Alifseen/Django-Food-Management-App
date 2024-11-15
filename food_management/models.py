from django.db import models
from django.contrib.auth.models import User

## Custom selection Variables. Tuple of Tuples
FOOD_TYPE = (
    ("starter", "Starter"),
    ("salads", "Salads"),
    ("entree","Entree"),
    ("dessert","Dessert")
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


# We need to create a food category, dishname, ingredients, and price column table
class Meals(models.Model):
    ## Crete columns for names, descriptions and price of the meals
    dish_name = models.CharField(max_length=1000, unique=True)
    ingredients = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    ## Create column for category of meal
    dish_category = models.CharField(max_length=200, choices=FOOD_TYPE)  ## This is a custom selection we create before the class in a constant Variable

    ## Create availability Status column
    availability = models.IntegerField(choices=STATUS, default=1)

    ## Create timestamps for creation and updates
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    ## Conecct a user to the meal so we know who added it
    chef = models.ForeignKey(User, on_delete=models.PROTECT)  ## CASCADE to delete if user deleted, SET_NULL to set user to null if user deleted

    def __str__(self):
        return self.dish_name