from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView

from .forms import MensajeForm
from .models import Mensaje


# cbv con mixin loginrequired para bandeja de entrada
class BandejaEntradaView(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'messaging/bandeja.html'
    context_object_name = 'mensajes'

    def get_queryset(self):
        return Mensaje.objects.filter(receptor=self.request.user).select_related('emisor')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        qs = self.get_queryset()
        ctx['no_leidos'] = qs.filter(leido=False).count()
        return ctx


# cbv con mixin loginrequired para enviar mensaje
class MensajeCreateView(LoginRequiredMixin, CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'messaging/enviar.html'
    success_url = '/mensajes/'

    def form_valid(self, form):
        form.instance.emisor = self.request.user
        messages.success(self.request, 'Mensaje enviado correctamente.')
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['receptor'].queryset = User.objects.exclude(pk=self.request.user.pk)
        return form


# fbv con decorador login_required para mensajes enviados
@login_required
def mensajes_enviados(request):
    mensajes = Mensaje.objects.filter(emisor=request.user).select_related('receptor')
    return render(request, 'messaging/enviados.html', {'mensajes': mensajes})


# fbv con decorador login_required para ver la conversacion
@login_required
def ver_conversacion(request, username):
    otro = get_object_or_404(User, username=username)

    mensajes = Mensaje.objects.filter(
        (Q(emisor=request.user) & Q(receptor=otro)) |
        (Q(emisor=otro) & Q(receptor=request.user))
    ).order_by('fecha_envio')

    Mensaje.objects.filter(emisor=otro, receptor=request.user, leido=False).update(leido=True)

    if request.method == 'POST':
        contenido = request.POST.get('contenido', '').strip()
        if contenido:
            Mensaje.objects.create(emisor=request.user, receptor=otro, contenido=contenido)
            messages.success(request, f'Mensaje enviado a {otro.username}.')
            return redirect('messaging:ver_conversacion', username=otro.username)

    return render(request, 'messaging/conversacion.html', {
        'otro': otro,
        'mensajes': mensajes,
    })
