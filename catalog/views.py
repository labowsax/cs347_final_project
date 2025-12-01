from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .forms import SignUpForm, FoodSearchForm
from .static.foodSearch import get_food_data
from .static.nutrient_functions import get_dv_avg
from django.core.paginator import Paginator
from django.core.cache import cache
import json
from datetime import datetime
# Create your views here.
from .models import Profile, FoodItem, LogItem


User = get_user_model()


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            birthdate = form.cleaned_data.get('birthdate')
            height = form.cleaned_data.get('height')
            weight = form.cleaned_data.get('weight')

            # check for existing username/email
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already taken.')
            elif User.objects.filter(email=email).exists():
                form.add_error('email', 'Email already registered.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                Profile.objects.create(user=user, birthdate=birthdate, height=height, weight=weight)
                # Log the user in and show a success message
                auth_login(request, user)
                messages.success(request, 'Account created and you are now logged in.')
                return HttpResponseRedirect(reverse('catalog:index'))
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


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


from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout


@login_required
def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None
    return render(request, 'profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    from .forms import ProfileForm

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return HttpResponseRedirect(reverse('catalog:profile'))
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile_edit.html', {'form': form})


def logout_view(request):
    """Log the user out and render a custom logged out page."""
    auth_logout(request)
    messages.info(request, "You've been logged out.")
    return render(request, 'logged_out.html')