from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.nutrient_gauge, name='index'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),
]
