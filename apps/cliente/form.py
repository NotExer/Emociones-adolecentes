from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # O puedes usar ['Emociones', 'Comentario']

        labels = {
            'Emociones': '¿Qué emoción sientes?',
            'Comentario': 'Comentario (opcional)',
        }

        widgets = {
            'Emociones': forms.Select(attrs={'class': 'form-control'}),
            'Comentario': forms.Textarea(attrs={
                'class': 'form-control',    
                'placeholder': 'Escribe un comentario si lo deseas...',
                'rows': 4
            }),
        }
