from django.contrib import admin

# Register your models here.
from .models import Weekday, Meal

admin.site.register(Weekday)
admin.site.register(Meal)
