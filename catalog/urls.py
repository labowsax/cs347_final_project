from django.urls import path
from .views import FoodItemListView

urlpatterns = [
    path("foods/", FoodItemListView.as_view(), name="food-list"),
]
