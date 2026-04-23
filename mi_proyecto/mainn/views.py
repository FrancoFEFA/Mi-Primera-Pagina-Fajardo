from django.shortcuts import render

from .models import Persona

from .forms import PersonaForm

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')


def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas.html', {'personas': personas})


def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'persona_creada.html')
    else:
        form = PersonaForm()
    return render(request, 'crear_persona.html', {'form': form})
