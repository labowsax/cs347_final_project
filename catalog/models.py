from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Django User already provides username, password, etc
# https://docs.djangoproject.com/en/5.2/ref/contrib/auth/
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None, height_field=None,
                              width_field=None, max_length=None)
    age = models.PositiveIntegerField(null=False)
    height = models.FloatField(null=False)
    weight = models.FloatField(null=False)
    gender = models.BooleanField(null=True)

    def __str__(self):
        return self.user.username


class FoodItem(models.Model):
    foodName = models.CharField(null=False, max_length=127)
    # Nutrients
    fat = models.FloatField(default=0)
    saturatedFat = models.FloatField(default=0)
    transFat = models.FloatField(default=0)
    cholesterol = models.FloatField(default=0)
    sodium = models.FloatField(default=0)
    carbohydrates = models.FloatField(default=0)
    fiber = models.FloatField(default=0)
    sugars = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    calcium = models.FloatField(default=0)
    iron = models.FloatField(default=0)
    potassium = models.FloatField(default=0)
    magnesium = models.FloatField(default=0)
    phosphorus = models.FloatField(default=0)
    zinc = models.FloatField(default=0)
    calories = models.FloatField(default=0)
    vitaminC = models.FloatField(default=0)
    vitaminD = models.FloatField(default=0)

    def __str__(self):
        return self.foodName


class LogItem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.models.DateTimeField(auto_now=False, auto_now_add=False)
    foodItem = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    # I assume use a float from 0 to 1
    percentConsumed = models.FloatField(default=1)

    def __str__(self):
        return (self.profile + ":" + self.FoodItem + ":" + self.date)
