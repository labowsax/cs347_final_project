from django import forms
from .models import LogItem
from datetime import datetime

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


class DateConsumedForm(forms.ModelForm):
    class Meta:
        model = LogItem
        fields = ['date']

    def clean_dateConsumed(self):
        value = self.cleaned_data.get('date')
        print(type(value))
        if value is None:
            raise forms.ValidationError("Oh boy.")
        if not (isinstance(value, datetime)):
            raise forms.ValidationError("Date must be a date-time")
        return value