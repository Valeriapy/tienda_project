from django import forms
from .models import Remera

class RemeraForm(forms.ModelForm):
    class Meta:
        model = Remera
        fields = ['marca', 'talle', 'color', 'lisa', 'genero']
        widgets = {
            'talle': forms.Select(),
            'genero': forms.Select(),
            'lisa': forms.CheckboxInput(),
        }
