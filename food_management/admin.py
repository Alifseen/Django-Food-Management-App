from django.contrib import admin
from.models import Meals

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("dish_name", "dish_category", "availability")
    list_filter = ("availability", )
    search_fields = ("dish_name", "ingredients")

admin.site.register(Meals, MenuItemAdmin)