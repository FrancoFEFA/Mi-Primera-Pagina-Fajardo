from django import forms
from .models import Mensaje


class MensajeForm(forms.ModelForm):
    """Formulario para enviar un nuevo mensaje a otro usuario."""

    class Meta:
        model = Mensaje
        fields = ['receptor', 'contenido']
        labels = {
            'receptor': 'Destinatario',
            'contenido': 'Mensaje',
        }
        widgets = {
            'receptor': forms.Select(attrs={'class': 'form-select'}),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribí tu mensaje...',
            }),
        }
