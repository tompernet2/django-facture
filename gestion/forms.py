from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'prix', 'date_peremption']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded'}),
            'prix': forms.NumberInput(attrs={'class': 'w-full px-4 py-2 border rounded'}),
            'date_peremption': forms.DateInput(
                attrs={
                    'type': 'date', 
                    'class': 'w-full px-4 py-2 border rounded'
                }
            ),
        }
