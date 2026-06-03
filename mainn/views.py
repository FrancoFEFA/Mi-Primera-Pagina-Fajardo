from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView

from .forms import (
    AsistenciaForm,
    AvatarForm,
    BuscarRutinaForm,
    EntrenadorForm,
    FotoEntrenadorForm,
    RutinaForm,
    SocioForm,
)
from .models import Asistencia, Entrenador, Rutina, Socio


def inicio(request):
    """Vista de la página de inicio con estadísticas del gimnasio."""
    contexto = {
        'total_socios': Socio.objects.count(),
        'total_entrenadores': Entrenador.objects.count(),
        'total_rutinas': Rutina.objects.count(),
        'total_asistencias': Asistencia.objects.count(),
        'ultimas_asistencias': Asistencia.objects.select_related('socio').order_by('-fecha')[:5],
    }
    return render(request, 'inicio.html', contexto)


def acerca_de_mi(request):
    """Vista estática 'Acerca de mí' con info del proyecto y del autor."""
    return render(request, 'acerca_de_mi.html')


# ========================
# VISTAS DE SOCIOS
# ========================

def lista_socios(request):
    """Vista que muestra la lista de todos los socios registrados."""
    socios = Socio.objects.all().order_by('apellido', 'nombre')
    return render(request, 'socios/lista.html', {'socios': socios})


def detalle_socio(request, socio_id):
    """Vista de detalle de un socio específico (vista de detalle desde el listado)."""
    socio = get_object_or_404(Socio, id=socio_id)
    rutinas = socio.rutinas.select_related('entrenador').all()
    asistencias = socio.asistencias.all()[:10]
    return render(request, 'socios/detalle.html', {
        'socio': socio,
        'rutinas': rutinas,
        'asistencias': asistencias,
    })


def crear_socio(request):
    """Vista para dar de alta un nuevo socio."""
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Socio creado exitosamente.')
            return redirect('lista_socios')
        messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = SocioForm()
    return render(request, 'socios/crear.html', {'form': form})


# ========================
# VISTAS DE ENTRENADORES
# ========================

def lista_entrenadores(request):
    """Vista que muestra la lista de todos los entrenadores registrados."""
    entrenadores = Entrenador.objects.all().order_by('apellido', 'nombre')
    return render(request, 'entrenadores/lista.html', {'entrenadores': entrenadores})


def crear_entrenador(request):
    """Vista para dar de alta un nuevo entrenador."""
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entrenador creado exitosamente.')
            return redirect('lista_entrenadores')
        messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = EntrenadorForm()
    return render(request, 'entrenadores/crear.html', {'form': form})


def editar_entrenador(request, entrenador_id):
    entrenador = get_object_or_404(Entrenador, id=entrenador_id)
    if request.method == 'POST':
        form = EntrenadorForm(request.POST, instance=entrenador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Entrenador actualizado exitosamente.')
            return redirect('lista_entrenadores')
        messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = EntrenadorForm(instance=entrenador)
    return render(request, 'entrenadores/editar.html', {'form': form, 'entrenador': entrenador})


def eliminar_entrenador(request, entrenador_id):
    entrenador = get_object_or_404(Entrenador, id=entrenador_id)
    if request.method == 'POST':
        entrenador.delete()
        messages.success(request, 'Entrenador eliminado exitosamente.')
        return redirect('lista_entrenadores')
    return render(request, 'entrenadores/confirmar_eliminar.html', {'entrenador': entrenador})


# ========================
# VISTA DE FOTOS DE ENTRENADORES
# ========================

def upload_foto_entrenador(request, entrenador_id):
    entrenador = get_object_or_404(Entrenador, id=entrenador_id)
    if request.method == 'POST':
        form = FotoEntrenadorForm(request.POST, request.FILES, instance=entrenador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto actualizada exitosamente.')
            return redirect('lista_entrenadores')
        messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = FotoEntrenadorForm(instance=entrenador)
    return render(request, 'entrenadores/upload_foto.html', {'form': form, 'entrenador': entrenador})


def eliminar_foto_entrenador(request, entrenador_id):
    entrenador = get_object_or_404(Entrenador, id=entrenador_id)
    if entrenador.foto:
        entrenador.foto.delete()
    entrenador.foto = None
    entrenador.save()
    messages.success(request, 'Foto eliminada exitosamente.')
    return redirect('upload_foto_entrenador', entrenador_id=entrenador.id)


# ========================
# VISTAS DE RUTINAS (CBVs)
# ========================

class RutinaListView(ListView):
    """CBV #1: ListView con búsqueda por Q objects."""

    model = Rutina
    template_name = 'rutinas/lista.html'
    context_object_name = 'rutinas'

    def get_queryset(self):
        qs = Rutina.objects.select_related('entrenador').prefetch_related('socios').all()
        consulta = self.request.GET.get('consulta', '').strip()
        if consulta:
            qs = qs.filter(
                Q(nombre__icontains=consulta) |
                Q(entrenador__especialidad__icontains=consulta)
            )
        return qs.order_by('nombre')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_busqueda'] = BuscarRutinaForm(self.request.GET or None)
        ctx['consulta'] = self.request.GET.get('consulta', '').strip()
        return ctx


class RutinaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """CBV #2: DeleteView con mixins LoginRequiredMixin y UserPassesTestMixin."""

    model = Rutina
    template_name = 'rutinas/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_rutinas')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_login_url(self):
        return reverse('accounts:login')


def crear_rutina(request):
    """Vista para crear una nueva rutina de entrenamiento."""
    if request.method == 'POST':
        form = RutinaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rutina creada exitosamente.')
            return redirect('lista_rutinas')
        messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = RutinaForm()
    return render(request, 'rutinas/crear.html', {'form': form})


def editar_rutina(request, rutina_id):
    rutina = get_object_or_404(Rutina, id=rutina_id)
    if request.method == 'POST':
        form = RutinaForm(request.POST, instance=rutina)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rutina actualizada exitosamente.')
            return redirect('lista_rutinas')
        messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = RutinaForm(instance=rutina)
    return render(request, 'rutinas/editar.html', {'form': form, 'rutina': rutina})


def eliminar_rutina(request, rutina_id):
    rutina = get_object_or_404(Rutina, id=rutina_id)
    if request.method == 'POST':
        rutina.delete()
        messages.success(request, 'Rutina eliminada exitosamente.')
        return redirect('lista_rutinas')
    return render(request, 'rutinas/confirmar_eliminar.html', {'rutina': rutina})


def editar_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Socio actualizado exitosamente.')
            return redirect('lista_socios')
        messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'socios/crear.html', {'form': form})


def eliminar_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    if request.method == 'POST':
        socio.delete()
        messages.success(request, 'Socio eliminado exitosamente.')
        return redirect('lista_socios')
    return render(request, 'socios/confirmar_eliminar.html', {'socio': socio})


# ========================
# VISTAS DE AVATARES
# ========================

def upload_avatar(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=socio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avatar actualizado exitosamente.')
            return redirect('lista_socios')
        messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = AvatarForm(instance=socio)
    return render(request, 'socios/upload_avatar.html', {'form': form, 'socio': socio})


def eliminar_avatar(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    if socio.avatar:
        socio.avatar.delete()
    socio.avatar = None
    socio.save()
    messages.success(request, 'Avatar eliminado exitosamente.')
    return redirect('upload_avatar', socio_id=socio.id)


# ========================
# VISTAS DE ASISTENCIAS
# ========================

@login_required
def lista_asistencias(request):
    """FBV con decorador @login_required: solo usuarios autenticados pueden ver el listado."""
    asistencias = Asistencia.objects.select_related('socio').all().order_by('-fecha')
    return render(request, 'asistencias/lista.html', {'asistencias': asistencias})


def crear_asistencia(request):
    """Vista para registrar una nueva asistencia."""
    if request.method == 'POST':
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Asistencia registrada correctamente.')
            return redirect('lista_asistencias')
    else:
        form = AsistenciaForm()
    return render(request, 'asistencias/crear.html', {'form': form})


def eliminar_asistencia(request, asistencia_id):
    asistencia = get_object_or_404(Asistencia, id=asistencia_id)
    if request.method == 'POST':
        asistencia.delete()
        messages.success(request, 'Asistencia eliminada correctamente.')
        return redirect('lista_asistencias')
    return render(request, 'asistencias/confirmar_eliminar.html', {'asistencia': asistencia})


def checkin_rapido(request, socio_id):
    """Registra asistencia rápida para un socio con actividad 'musculacion' por defecto."""
    socio = get_object_or_404(Socio, id=socio_id)
    Asistencia.objects.create(socio=socio, tipo_actividad='musculacion')
    messages.success(request, f'Check-in registrado para {socio.nombre} {socio.apellido}.')
    return redirect('lista_socios')
