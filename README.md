# ⚡ PowerFit — Sistema de Gestión de Gimnasio

Sistema web de gestión integral para gimnasios desarrollado con **Django 6.0** y **Bootstrap 5.3**. Incluye CRUD completo de socios, entrenadores y rutinas, registro de asistencias con check-in rápido, gestión multimedia, búsqueda avanzada y notificaciones toast — todo con un diseño dark mode profesional.

---

## 🚀 Mejoras Implementadas (Versión Final)

### 📋 Formulario de Asistencia
- Vista `crear_asistencia` con template dedicado `asistencias/crear.html`
- URL `/asistencias/crear/` con nombre `crear_asistencia`
- Formulario `AsistenciaForm` con campos socio + tipo de actividad
- Widgets estilizados con Bootstrap (`form-select`)

### 🗑️ Eliminar Asistencia
- Vista `eliminar_asistencia` con confirmación previa
- Template `asistencias/confirmar_eliminar.html` con protección CSRF
- Botón de eliminación individual (ícono 🗑️) en cada fila de la lista
- Uso de `get_object_or_404` para seguridad

### ⚡ Check-in Rápido
- Nueva vista `/asistencias/checkin/<id>/` → registro instantáneo
- Actividad por defecto: Musculación
- Botón verde ✅ visible en cada fila de la lista de socios
- Redirección automática a lista de socios tras el registro

### 🔔 Mensajes Flash (Toasts)
- Sistema completo de notificaciones toast en `base.html`
- Íconos diferenciados: ✅ success, ⚠️ warning, ❌ danger, ℹ️ info
- Auto-desaparición a los 4 segundos con cierre manual
- Integrado en **todas** las vistas: crear, editar, eliminar, upload, checkin
- Mapeo `MESSAGE_TAGS = {ERROR: 'danger'}` en `settings.py`

### 🏠 Botón Inicio Mejorado
- "Asistencia +" ahora enlaza directamente a `crear_asistencia`
- Botones de acceso rápido: Alta Socio, Alta Entrenador, Crear Rutina
- Dashboard con últimas 5 asistencias en tiempo real

### 🔍 Búsqueda Avanzada de Rutinas
- Filtrado por nombre de rutina **o** especialidad del entrenador
- Uso de `Q objects` de Django para consultas OR
- Indicador de resultados y botón para limpiar búsqueda

### 📸 Gestión Multimedia
- Upload de avatar para socios y foto para entrenadores
- Visualización circular con bordes estilizados
- Eliminar foto sin afectar el registro del modelo
- Validación `accept="image/*"` en formularios

### 📊 Dashboard de Inicio
- 4 tarjetas de estadísticas en tiempo real (socios, entrenadores, rutinas, asistencias)
- Panel de accesos rápidos con íconos y descripciones
- Últimas 5 asistencias con `select_related` optimizado
- Hero section con gradiente y animación fadeInUp

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
|------------|-----------|
| Backend | Django 6.0.4 |
| Frontend | Bootstrap 5.3.3 + Bootstrap Icons 1.11.3 |
| Tipografía | Google Fonts (Inter) |
| Base de datos | SQLite3 |
| Imágenes | Pillow 12.2.0 |
| Idioma/Zona | es-ar / America/Argentina/Buenos_Aires |

---

## 📁 Estructura del Proyecto

```
Proyecto PowerFit Gym/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── mi_proyecto/              # Configuración Django
│   ├── settings.py           # MESSAGE_TAGS, MEDIA config
│   ├── urls.py               # include('mainn.urls') + media
│   └── wsgi/asgi.py
├── mainn/                    # App principal
│   ├── models.py             # 4 modelos: Socio, Entrenador, Rutina, Asistencia
│   ├── views.py              # 17 vistas (CRUD + upload + checkin)
│   ├── forms.py              # 7 formularios con widgets Bootstrap
│   ├── urls.py               # 18 rutas con nombres descriptivos
│   └── admin.py              # 4 modelos registrados
├── templates/
│   ├── base.html             # Layout + navbar + toasts + footer (569 líneas)
│   ├── inicio.html           # Dashboard con estadísticas
│   ├── socios/               # crear, lista, upload_avatar, confirmar_eliminar
│   ├── entrenadores/         # crear, editar, lista, upload_foto, confirmar_eliminar
│   ├── rutinas/              # crear, editar, lista, confirmar_eliminar
│   └── asistencias/          # crear, lista, confirmar_eliminar
└── media/                    # Avatares y fotos subidas
```

---

## 🎨 Diseño UI/UX

- **Dark mode** profesional con paleta personalizada (CSS variables)
- Navbar sticky con glassmorphism (`backdrop-filter: blur`)
- Tarjetas con hover animado y bordes con gradiente
- Badges de colores por membresía (Básica / Premium / VIP) y turno (Mañana / Tarde / Noche)
- Animaciones `fadeInUp` escalonadas en listas
- Scrollbar personalizado
- Empty states descriptivos con CTAs
- Diseño 100% responsive (mobile-first)

---

## 🔧 Instalación

```bash
# Clonar repositorio
git clone [URL_DEL_REPOSITORIO]
cd "Proyecto PowerFit Gym"

# Entorno virtual
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # Linux/Mac

# Dependencias
pip install -r requirements.txt

# Base de datos
python manage.py migrate

# Superusuario
python manage.py createsuperuser

# Servidor
python manage.py runserver
```

### URLs del sistema
| Ruta | Descripción |
|------|-------------|
| `/` | Dashboard principal |
| `/socios/` | Gestión de socios |
| `/entrenadores/` | Gestión de entrenadores |
| `/rutinas/` | Gestión de rutinas + buscador |
| `/asistencias/` | Registro de asistencias |
| `/asistencias/checkin/<id>/` | Check-in rápido |
| `/admin/` | Panel de administración Django |

---

## 💡 Aspectos Técnicos Destacados

- ✅ Patrón **MTV** de Django aplicado correctamente
- ✅ `select_related` / `prefetch_related` para optimizar queries
- ✅ `get_object_or_404` para manejo seguro de errores
- ✅ `Q objects` para búsquedas OR complejas
- ✅ `messages.success` / `messages.error` en todas las operaciones
- ✅ Templates con herencia (`base.html` → child templates)
- ✅ URLs RESTful con nombres semánticos
- ✅ Formularios ModelForm con validación server-side
- ✅ Servicio de archivos media en desarrollo (`static()`)
- ✅ Código documentado con docstrings y comentarios

---

**Versión:** 2.0.0 — Entrega Final  
**Última actualización:** 14 de mayo de 2026  
**Estado:** ✅ Producción lista