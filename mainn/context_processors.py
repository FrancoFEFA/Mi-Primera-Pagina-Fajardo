"""Context processor que expone al template qué sección del navbar está activa."""


def nav_active(request):
    """Devuelve un dict con las secciones activas según el URL name actual."""
    sections = {
        'socios': {
            'lista_socios', 'crear_socio', 'detalle_socio',
            'upload_avatar', 'eliminar_avatar',
            'editar_socio', 'eliminar_socio',
        },
        'entrenadores': {
            'lista_entrenadores', 'crear_entrenador', 'editar_entrenador',
            'upload_foto_entrenador', 'eliminar_foto_entrenador',
            'eliminar_entrenador',
        },
        'rutinas': {
            'lista_rutinas', 'crear_rutina', 'editar_rutina', 'eliminar_rutina',
        },
        'asistencias': {
            'lista_asistencias', 'crear_asistencia',
            'checkin_rapido', 'eliminar_asistencia',
        },
        'mensajes': {
            'bandeja', 'enviar', 'enviados', 'ver_conversacion',
        },
    }

    current = request.resolver_match.url_name if request.resolver_match else None
    return {
        'active_nav': {key: current in urls for key, urls in sections.items()},
    }
