from django.contrib import admin
from .models import FoodItem, LogItem, Profile

# Register your models here.


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('foodName', 'fdcId')


@admin.register(LogItem)
class LogItemAdmin(admin.ModelAdmin):
    list_display = ('profile', 'date')


admin.site.register(Profile)
