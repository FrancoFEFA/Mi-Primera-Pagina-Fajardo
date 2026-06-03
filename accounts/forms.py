from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegistroForm(UserCreationForm):
    """Formulario de registro de nuevos usuarios."""

    email = forms.EmailField(required=True, label='Correo electrónico')
    first_name = forms.CharField(max_length=50, required=True, label='Nombre')
    last_name = forms.CharField(max_length=50, required=True, label='Apellido')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            widget = field.widget
            if isinstance(widget, forms.TextInput) or isinstance(widget, forms.EmailInput) or isinstance(widget, forms.PasswordInput):
                widget.attrs.setdefault('class', 'form-control')
            placeholder_map = {
                'username': 'Ej: juanperez',
                'first_name': 'Tu nombre',
                'last_name': 'Tu apellido',
                'email': 'ejemplo@correo.com',
            }
            if field_name in placeholder_map:
                widget.attrs.setdefault('placeholder', placeholder_map[field_name])

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Profile.objects.get_or_create(user=user)
        return user


class ProfileForm(forms.ModelForm):
    """Formulario para editar el perfil extendido del usuario."""

    first_name = forms.CharField(max_length=50, required=True, label='Nombre')
    last_name = forms.CharField(max_length=50, required=True, label='Apellido')
    email = forms.EmailField(required=True, label='Correo electrónico')

    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'fecha_nacimiento', 'ciudad']
        labels = {
            'avatar': 'Foto de perfil',
            'bio': 'Biografía',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'ciudad': 'Ciudad',
        }
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'},
                format='%Y-%m-%d',
            ),
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: Buenos Aires'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email
        for field_name in ['first_name', 'last_name', 'email']:
            self.fields[field_name].widget.attrs.setdefault('class', 'form-control')

    def save(self, commit=True):
        profile = super().save(commit=False)
        if profile.user:
            profile.user.first_name = self.cleaned_data['first_name']
            profile.user.last_name = self.cleaned_data['last_name']
            profile.user.email = self.cleaned_data['email']
            if commit:
                profile.user.save()
                profile.save()
        return profile
