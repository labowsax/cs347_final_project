from django.db import models
import uuid

# Create your models here.


class FoodItem(models.Model):
    foodName = models.CharField(max_length=127)
    dateTime = models.DateTimeField(auto_now_add=True)
    # Nutrients
    fat = models.FloatField(null=True, blank=True)
    saturatedFat = models.FloatField(null=True, blank=True)
    transFat = models.FloatField(null=True, blank=True)
    cholesterol = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    carbohydrates = models.FloatField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    sugars = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    calcium = models.FloatField(null=True, blank=True)
    iron = models.FloatField(null=True, blank=True)
    calories = models.FloatField(null=True, blank=True)
    vitaminA = models.FloatField(null=True, blank=True)
    vitaminC = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.foodName
