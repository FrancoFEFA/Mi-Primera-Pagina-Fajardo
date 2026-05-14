from django.shortcuts import render, redirect
from django.db.models import Q

from .models import Socio, Entrenador, Rutina, Asistencia
from .forms import SocioForm, EntrenadorForm, RutinaForm, BuscarRutinaForm, AvatarForm


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


# ========================
# VISTAS DE SOCIOS
# ========================

def lista_socios(request):
    """Vista que muestra la lista de todos los socios registrados."""
    socios = Socio.objects.all().order_by('apellido', 'nombre')
    return render(request, 'socios/lista.html', {'socios': socios})


def crear_socio(request):
    """Vista para dar de alta un nuevo socio."""
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_socios')
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
            return redirect('lista_entrenadores')
    else:
        form = EntrenadorForm()
    return render(request, 'entrenadores/crear.html', {'form': form})


# ========================
# VISTAS DE RUTINAS
# ========================

def lista_rutinas(request):
    """Vista que muestra las rutinas con buscador integrado usando Q de Django."""
    form_busqueda = BuscarRutinaForm(request.GET or None)
    rutinas = Rutina.objects.select_related('entrenador').prefetch_related('socios').all()

    consulta = request.GET.get('consulta', '').strip()
    if consulta:
        rutinas = rutinas.filter(
            Q(nombre__icontains=consulta) |
            Q(entrenador__especialidad__icontains=consulta)
        )

    contexto = {
        'rutinas': rutinas.order_by('nombre'),
        'form_busqueda': form_busqueda,
        'consulta': consulta,
    }
    return render(request, 'rutinas/lista.html', contexto)


def crear_rutina(request):
    """Vista para crear una nueva rutina de entrenamiento."""
    if request.method == 'POST':
        form = RutinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_rutinas')
    else:
        form = RutinaForm()
    return render(request, 'rutinas/crear.html', {'form': form})


# ========================
# VISTA DE AVATARES
# ========================

def upload_avatar(request, socio_id):
    socio = Socio.objects.get(id=socio_id)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('lista_socios')
    else:
        form = AvatarForm(instance=socio)
    return render(request, 'socios/upload_avatar.html', {'form': form, 'socio': socio})


def eliminar_avatar(request, socio_id):
    socio = Socio.objects.get(id=socio_id)
    if socio.avatar:
        socio.avatar.delete()
    socio.avatar = None
    socio.save()
    return redirect('upload_avatar', socio_id=socio.id)


# ========================
# VISTAS DE ASISTENCIAS
# ========================

def lista_asistencias(request):
    """Vista que muestra la lista de todas las asistencias registradas."""
    asistencias = Asistencia.objects.select_related('socio').all().order_by('-fecha')
    return render(request, 'asistencias/lista.html', {'asistencias': asistencias})
