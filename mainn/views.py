from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models import Socio, Entrenador, Rutina, Asistencia
from .forms import SocioForm, EntrenadorForm, RutinaForm, BuscarRutinaForm, AvatarForm, FotoEntrenadorForm


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


def editar_entrenador(request, entrenador_id):
    entrenador = Entrenador.objects.get(id=entrenador_id)
    if request.method == 'POST':
        form = EntrenadorForm(request.POST, instance=entrenador)
        if form.is_valid():
            form.save()
            return redirect('lista_entrenadores')
    else:
        form = EntrenadorForm(instance=entrenador)
    return render(request, 'entrenadores/editar.html', {'form': form, 'entrenador': entrenador})


def eliminar_entrenador(request, entrenador_id):
    entrenador = get_object_or_404(Entrenador, id=entrenador_id)
    if request.method == 'POST':
        entrenador.delete()
        return redirect('lista_entrenadores')
    return render(request, 'entrenadores/confirmar_eliminar.html', {'entrenador': entrenador})


# ========================
# VISTA DE FOTOS DE ENTRENADORES
# ========================

def upload_foto_entrenador(request, entrenador_id):
    entrenador = Entrenador.objects.get(id=entrenador_id)
    if request.method == 'POST':
        form = FotoEntrenadorForm(request.POST, request.FILES, instance=entrenador)
        if form.is_valid():
            form.save()
            return redirect('lista_entrenadores')
    else:
        form = FotoEntrenadorForm(instance=entrenador)
    return render(request, 'entrenadores/upload_foto.html', {'form': form, 'entrenador': entrenador})


def eliminar_foto_entrenador(request, entrenador_id):
    entrenador = Entrenador.objects.get(id=entrenador_id)
    if entrenador.foto:
        entrenador.foto.delete()
    entrenador.foto = None
    entrenador.save()
    return redirect('upload_foto_entrenador', entrenador_id=entrenador.id)


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


def editar_rutina(request, rutina_id):
    rutina = Rutina.objects.get(id=rutina_id)
    if request.method == 'POST':
        form = RutinaForm(request.POST, instance=rutina)
        if form.is_valid():
            form.save()
            return redirect('lista_rutinas')
    else:
        form = RutinaForm(instance=rutina)
    return render(request, 'rutinas/editar.html', {'form': form, 'rutina': rutina})


def eliminar_rutina(request, rutina_id):
    rutina = Rutina.objects.get(id=rutina_id)
    if request.method == 'POST':
        rutina.delete()
        return redirect('lista_rutinas')
    return render(request, 'rutinas/confirmar_eliminar.html', {'rutina': rutina})


def editar_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    if request.method == 'POST':
        form = SocioForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            return redirect('lista_socios')
    else:
        form = SocioForm(instance=socio)
    return render(request, 'socios/crear.html', {'form': form})


def eliminar_socio(request, socio_id):
    socio = get_object_or_404(Socio, id=socio_id)
    if request.method == 'POST':
        socio.delete()
        return redirect('lista_socios')
    return render(request, 'socios/confirmar_eliminar.html', {'socio': socio})


# ========================
# VISTAS DE AVATARES
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
