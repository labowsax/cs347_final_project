from django.urls import path
from . import views

urlpatterns = [
    path('', views.nutrient_gauge, name='index'),
    path('search/', views.search, name='search'),
]
