from django import forms
from .models import mascotas

class MascotaForm(forms.ModelForm):
    class Meta: 
        model = mascotas
        fields = '__all__'

