from django.shortcuts import render, redirect, get_object_or_404
from .static.foodSearch import get_food_data
from .static.nutrient_functions import get_dv_avg, get_log_items
from django.core.paginator import Paginator
from django.core.cache import cache
import json
from datetime import datetime
# Create your views here.
from .models import Profile, FoodItem, LogItem
from .forms import PercentConsumedForm



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


def index(request):
    """View function for home page of site."""
    start = datetime(2025, 11, 1, 15, 30)  # year, month, day, hour, minute
    end = datetime(2025, 11, 8, 15, 30)  # year, month, day, hour, minute
    nutrients = get_dv_avg(start, end, 1)
    
    context = {
        'nutrients': nutrients
    }

    return render(request, 'index.html', context=context)

def edit(request):
    """View function for home page of site."""
    start = datetime(2024, 11, 1, 15, 30)  # year, month, day, hour, minute
    end = datetime(2026, 11, 8, 15, 30)  # year, month, day, hour, minute
    nutrients = get_dv_avg(start, end, 1)
    LogItems = get_log_items(start, end, 1)
    
    context = {
        'LogItems': LogItems
    }

    return render(request, 'edit.html', context)

def update_percent(request, log_id):
    log_item = get_object_or_404(LogItem, id=log_id)

    if request.method == 'POST':
        form = PercentConsumedForm(request.POST, instance=log_item)
        if form.is_valid():
            form.save()
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            # Optionally, you can pass errors back to template
            return render(request, 'your_template.html', {'form': form, 'log_item': log_item})