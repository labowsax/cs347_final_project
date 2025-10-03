from . models import FoodItem
from rest_framework import generics
from . serializer import FoodItemSerializer
# Create your views here.


class FoodItemListView(generics.ListAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
