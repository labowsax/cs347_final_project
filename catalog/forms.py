from django import forms
from .models import Profile


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

class SignUpForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=150, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True, min_length=8)
    birthdate = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    height = forms.FloatField(required=True, min_value=0.0,
                              widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}))
    weight = forms.FloatField(required=True, min_value=0.0,
                              widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalnum():
            raise forms.ValidationError("Username must be alphanumeric.")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password

    def clean_height(self):
        height = self.cleaned_data['height']
        if height <= 0:
            raise forms.ValidationError("Height must be a positive number.")
        return height

    def clean_weight(self):
        weight = self.cleaned_data['weight']
        if weight <= 0:
            raise forms.ValidationError("Weight must be a positive number.")
        return weight


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birthdate', 'height', 'weight', 'gender', 'image']
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }