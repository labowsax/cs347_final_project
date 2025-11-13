from django import forms
from .models import LogItem

class PercentConsumedForm(forms.ModelForm):
    class Meta:
        model = LogItem
        fields = ['percentConsumed']

    def clean_percentConsumed(self):
        value = self.cleaned_data.get('percentConsumed')
        if value is None:
            raise forms.ValidationError("Oh boy.")
        if value < 0 or value > 1000:
            raise forms.ValidationError("Percent must be between 0 and 1000.")
        return value
