from django import forms


class FoodSearchForm(forms.Form):
    query = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search here!',
            'aria-label': 'Search',
        })
    )
