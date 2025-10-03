from rest_framework import serializers
from . models import FoodItem


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ['id',
                  'foodName',
                  'fat',
                  'saturatedFat',
                  'transFat',
                  'cholesterol',
                  'sodium',
                  'carbohydrates',
                  'fiber',
                  'sugars',
                  'protein',
                  'calcium',
                  'iron',
                  'calories',
                  'vitaminA',
                  'vitaminC'
                  ]
