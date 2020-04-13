from django.forms import ModelForm
from .models import Print

class NewPrint(ModelForm):
    class Meta:
        model = Print
        fields = ['date', 'cover']