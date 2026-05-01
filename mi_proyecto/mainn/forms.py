from django import forms
from .models import Socio, Entrenador, Rutina


class SocioForm(forms.ModelForm):
    """Formulario para dar de alta un nuevo socio."""

    class Meta:
        model = Socio
        fields = ['nombre', 'apellido', 'email', 'tipo_membresia']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del socio',
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido del socio',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com',
            }),
            'tipo_membresia': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'email': 'Correo electrónico',
            'tipo_membresia': 'Tipo de membresía',
        }


class EntrenadorForm(forms.ModelForm):
    """Formulario para dar de alta un nuevo entrenador."""

    class Meta:
        model = Entrenador
        fields = ['nombre', 'apellido', 'especialidad', 'email', 'turno']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del entrenador',
            }),
            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Apellido del entrenador',
            }),
            'especialidad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Musculación, CrossFit, Yoga...',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com',
            }),
            'turno': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'especialidad': 'Especialidad',
            'email': 'Correo electrónico',
            'turno': 'Turno',
        }


class RutinaForm(forms.ModelForm):
    """Formulario para crear una nueva rutina de entrenamiento."""

    class Meta:
        model = Rutina
        fields = ['nombre', 'descripcion', 'duracion_semanas', 'entrenador', 'socios']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la rutina',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción detallada de la rutina...',
                'rows': 4,
            }),
            'duracion_semanas': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duración en semanas',
                'min': 1,
            }),
            'entrenador': forms.Select(attrs={
                'class': 'form-select',
            }),
            'socios': forms.SelectMultiple(attrs={
                'class': 'form-select',
                'size': 5,
            }),
        }
        labels = {
            'nombre': 'Nombre de la rutina',
            'descripcion': 'Descripción',
            'duracion_semanas': 'Duración (semanas)',
            'entrenador': 'Entrenador asignado',
            'socios': 'Socios asignados',
        }


class BuscarRutinaForm(forms.Form):
    """Formulario de búsqueda de rutinas por nombre o especialidad del entrenador."""

    consulta = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar por nombre de rutina o especialidad del entrenador...',
        }),
        label='Buscar rutina',
    )
