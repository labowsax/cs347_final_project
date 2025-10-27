from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.blank_search, name='search'),
    path('search/<slug:slug>/', views.search, name='search'),
]
