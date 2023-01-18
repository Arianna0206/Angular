from django import forms
from .models import agendas


class AgendaForm(forms.ModelForm):
    class Meta: 
        model = agendas
        fields = '__all__'

    