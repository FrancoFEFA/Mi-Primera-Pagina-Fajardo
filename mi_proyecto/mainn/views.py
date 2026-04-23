from django.shortcuts import render

from .models import Persona

def inicio(request):
    return render(request, 'inicio.html')


def lista_personas(request):
    personas = Persona.objects.all()
    return render(request, 'personas.html', {'personas': personas})

# Create your views here.
