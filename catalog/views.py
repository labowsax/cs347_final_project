from django.shortcuts import render
from .static.foodSearch import get_food_data
from .static.nutrient_functions import get_dv_avg
from django.core.paginator import Paginator
from django.core.cache import cache
import json
from datetime import datetime
# Create your views here.
from .models import Profile, FoodItem, LogItem
from .forms import FoodSearchForm


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


def search(request):
    query = request.GET.get("q")
    foods = []

    if query:
        cache_key = f"food_results_{query.lower()}"
        foods = cache.get(cache_key)

        if not foods:
            foods = get_food_data(query)
            cache.set(cache_key, foods, timeout=60 * 60)  # Cache for 1 hour

    paginator = Paginator(foods, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'search.html', {"page_obj": page_obj, "query": query})


def nutrient_gauge(request):
    """View function for home page of site."""
    start = datetime(2025, 11, 1, 15, 30)  # year, month, day, hour, minute
    end = datetime(2025, 11, 8, 15, 30)  # year, month, day, hour, minute
    nutrients = get_dv_avg(start, end, 1)
    
    context = {
        'nutrients': nutrients
    }

    return render(request, '_nutrient_gauge.html', context=context)