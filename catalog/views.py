from django.shortcuts import render
from .static.foodSearch import get_food_data
import json
# Create your views here.
from .models import Profile, FoodItem, LogItem


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_food_items = FoodItem.objects.all().count()
    num_instances = LogItem.objects.all().count()
    num_profiles = Profile.objects.all().count()

    context = {
        'num_food_items': num_food_items,
        'num_instances': num_instances,
        'num_profiles': num_profiles,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def blank_search(request):
    """View function for search page of site."""
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'search.html', context=None)


def search(request, slug):
    """View function for search page of site."""
    food_data = get_food_data(slug)
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'search.html', context=food_data)
