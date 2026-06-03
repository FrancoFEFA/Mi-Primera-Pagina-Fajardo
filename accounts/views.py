from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from .forms import ProfileForm, RegistroForm
from .models import Profile


class RegistroView(CreateView):
    """CBV para registro de nuevos usuarios."""

    form_class = RegistroForm
    template_name = 'accounts/registro.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, f'¡Bienvenido, {self.object.username}! Tu cuenta fue creada.')
        return response

    def form_invalid(self, form):
        messages.error(self.request, 'Revisá los datos del formulario. Hay errores.')
        return super().form_invalid(form)


class CustomLoginView(LoginView):
    """Login con mensajes toast."""

    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, f'¡Hola de nuevo, {form.get_user().username}!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Usuario o contraseña incorrectos.')
        return super().form_invalid(form)


@login_required
def logout_view(request):
    """FBV con decorador login_required para cerrar sesión."""
    logout(request)
    messages.info(request, 'Cerraste sesión correctamente.')
    return redirect('inicio')


@method_decorator(login_required, name='dispatch')
class ProfileUpdateView(UpdateView):
    """CBV con mixin LoginRequired (vía method_decorator) y LoginRequiredMixin implícito."""

    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/editar_perfil.html'
    success_url = '/cuentas/perfil/'

    def get_object(self, queryset=None):
        profile, _ = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        messages.success(self.request, 'Perfil actualizado correctamente.')
        return super().form_valid(form)


@login_required
def perfil_view(request):
    """FBV con decorador login_required para mostrar el perfil del usuario."""
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/perfil.html', {'profile': profile})


def perfil_publico(request, username):
    """FBV que muestra el perfil público de cualquier usuario."""
    user = get_object_or_404(User, username=username)
    profile, _ = Profile.objects.get_or_create(user=user)
    return render(request, 'accounts/perfil_publico.html', {'profile': profile, 'perfil_user': user})
