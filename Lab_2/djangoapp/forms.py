from django import forms
from djangoapp.models import Measurement

class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['value', 'description', 'time']
