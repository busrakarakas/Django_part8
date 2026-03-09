from django import forms
from .models import TeknoProje

class TeknoProjeForm(forms.ModelForm):
    class Meta:
        model = TeknoProje
        fields = ['baslik', 'detay', 'durum', 'resim']
        widgets = {
            'baslik': forms.TextInput(attrs={'class': 'glass-input'}),
            'detay': forms.Textarea(attrs={'class': 'glass-input', 'rows': 4}),
            'durum': forms.CheckboxInput(attrs={'class': 'glass-checkbox'}), # Burası kutucuğa çevirir
            'resim': forms.FileInput(attrs={'class': 'glass-input'}),
        }