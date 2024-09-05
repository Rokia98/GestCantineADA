from django import forms
from .models import PlatModel

class PlatForm(forms.ModelForm):
    class Meta:
        model = PlatModel
        fields = '__all__' # Les champs spécifiques à MenuModel

