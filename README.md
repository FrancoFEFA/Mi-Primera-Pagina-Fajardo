# ⚡ PowerFit — Sistema de Gestión de Gimnasio

Sistema web de gestión integral para gimnasios desarrollado con **Django 6.0** y **Bootstrap 5.3**. Incluye CRUD completo de socios, entrenadores y rutinas, registro de asistencias con check-in rápido, gestión multimedia, búsqueda avanzada, autenticación de usuarios, mensajería interna y notificaciones toast — todo con un diseño dark mode profesional.

---

## 🚀 Mejoras Implementadas (Versión Final)

### 🔐 Sistema de Autenticación Completo
- App nueva `accounts` con registro, login, logout, perfil y edición de perfil
- Vista de registro como **CBV** (`CreateView`) con creación automática de `Profile` vía `post_save` signal
- Login como **CBV** (`LoginView` personalizado) con mensajes de bienvenida
- Logout como **FBV** protegido con el **decorador `@login_required`**
- Edición de perfil como **CBV** (`UpdateView`) con `LoginRequiredMixin`
- Perfil público accesible por username (`/cuentas/perfil/<username>/`)
- Modelo `Profile` extendido con avatar, biografía, fecha de nacimiento y ciudad
- Navbar con dropdown de usuario, botón "Ingresar" y "Registrarse" según estado de sesión
- `LOGIN_URL`, `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL` configurados en `settings.py`

### 🏗️ Vistas Basadas en Clases (CBV)
- `RutinaListView` (`ListView`) con búsqueda integrada por `Q objects`
- `RutinaDeleteView` (`DeleteView`) con **mixins** `LoginRequiredMixin` y `UserPassesTestMixin` (solo staff puede eliminar)
- `RegistroView` y `ProfileUpdateView` en `accounts`
- `BandejaEntradaView` y `MensajeCreateView` en `messaging`
- `method_decorator(login_required)` aplicado en CBVs donde se necesita

### ✉️ App de Mensajería Interna
- App nueva `messaging` con modelo `Mensaje` (emisor, receptor, contenido, fecha, leído)
- Bandeja de entrada como **CBV** (`ListView`) con contador de no leídos
- Envío de mensajes como **CBV** (`CreateView`) con queryset filtrado (excluye al usuario actual)
- Listado de mensajes enviados como **FBV** protegido con `@login_required`
- Vista de conversación 1-a-1 con burbujas tipo chat (derecha/izquierda según emisor)
- Auto-marcado de mensajes como leídos al abrir la conversación
- Registrar en `/admin/` con búsqueda por emisor/receptor/contenido

### 👁️ Vista de Detalle de Socio
- Nueva vista `detalle_socio` con URL `/socios/<id>/`
- Card lateral con avatar, datos de contacto, membresía y acciones rápidas
- Sección de rutinas asignadas con `select_related('entrenador')`
- Sección de últimas 10 asistencias
- Link clickeable desde el listado y desde "Últimas Asistencias" del dashboard

### ℹ️ Vista "Acerca"
- Página estática `/acerca-de-mi/` con información del proyecto y del autor
- Secciones: descripción general, funcionalidades principales, stack tecnológico y datos del autor
- Diseño consistente con la línea visual dark mode del proyecto

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
- Integrado en **todas** las vistas: crear, editar, eliminar, upload, checkin, login, registro, mensajería
- Mapeo `MESSAGE_TAGS = {ERROR: 'danger'}` en `settings.py`

### 🏠 Botón Inicio Mejorado
- "Asistencia +" ahora enlaza directamente a `crear_asistencia`
- Botones de acceso rápido: Alta Socio, Alta Entrenador, Crear Rutina
- Dashboard con últimas 5 asistencias en tiempo real (clickeables → detalle del socio)

### 🔍 Búsqueda Avanzada de Rutinas
- Filtrado por nombre de rutina **o** especialidad del entrenador
- Uso de `Q objects` de Django para consultas OR
- Indicador de resultados y botón para limpiar búsqueda
- Implementada como `ListView` (CBV) con `get_queryset` y `get_context_data`

### 📸 Gestión Multimedia
- Upload de avatar para socios y foto para entrenadores
- Visualización circular con bordes estilizados
- Eliminar foto sin afectar el registro del modelo
- Validación `accept="image/*"` en formularios
- Avatares de perfil de usuario (`accounts.Profile.avatar`)

### 📊 Dashboard de Inicio
- 4 tarjetas de estadísticas en tiempo real (socios, entrenadores, rutinas, asistencias)
- Panel de accesos rápidos con íconos y descripciones
- Últimas 5 asistencias con `select_related` optimizado y link a detalle del socio
- Hero section con gradiente y animación fadeInUp

---

## ✨ Características

### 🧑‍💼 Gestión de Socios
- Registrar nuevos socios
- Asignar tipos de membresía (Básica, Premium, VIP)
- Listar todos los socios registrados
- **Ver detalle del socio** con rutinas asignadas e historial de asistencias
- Ver información detallada: nombre, apellido, email, tipo de membresía
- Registro automático de fecha de inscripción
- **Upload de avatar** con visualización circular
- **Check-in rápido** para registrar asistencia al instante
- Editar y eliminar socios con confirmación

### 👨‍🏫 Gestión de Entrenadores
- Registrar entrenadores con especialidades
- Asignar turnos de trabajo (Mañana, Tarde, Noche)
- Listar todos los entrenadores
- Registrar email de contacto
- **Upload de foto** de perfil
- Editar y eliminar entrenadores

### 💪 Gestión de Rutinas
- Crear rutinas de entrenamiento personalizadas
- Asignar rutinas a entrenadores
- Vincular rutinas a socios
- Especificar duración de las rutinas (en semanas)
- **Búsqueda avanzada** por nombre de rutina o especialidad del entrenador
- Editar rutinas (FBV) y **eliminar rutinas** (CBV con mixins, solo staff)
- Vista de listado implementada como `ListView` con paginación nativa de Django

### 📊 Registro de Asistencias
- Registrar asistencias de socios
- Categorizar por tipo de actividad (Musculación, Cardio, CrossFit, Yoga, Spinning, Funcional)
- Listar historial de asistencias ordenado por fecha (requiere autenticación)
- **Check-in rápido** desde lista de socios
- **Eliminar asistencia** con confirmación
- Visualizar las últimas 5 asistencias en la página de inicio

### 🔐 Autenticación y Perfiles
- Registro de usuarios con email, nombre y apellido
- Inicio y cierre de sesión con mensajes toast
- Perfil extendido (`Profile`) con avatar, bio, fecha de nacimiento y ciudad
- Edición completa del perfil (datos de User + Profile en un único formulario)
- Perfiles públicos accesibles por username
- Creación automática de `Profile` al registrar un nuevo usuario (`post_save` signal)

### ✉️ Mensajería Interna
- Bandeja de entrada con indicador de mensajes no leídos
- Envío de mensajes a cualquier usuario del sistema
- Listado de mensajes enviados
- Vista de conversación 1-a-1 con burbujas estilo chat
- Marcado automático como leído al abrir la conversación
- Acceso desde el navbar (requiere autenticación)

### 📈 Panel de Estadísticas
- Página de inicio con estadísticas generales:
  - Total de socios registrados
  - Total de entrenadores
  - Total de rutinas
  - Total de asistencias
  - Últimas asistencias registradas (con link a detalle)

### 🔔 Sistema de Notificaciones
- Mensajes toast success/error/warning/info
- Auto-desaparición a los 4 segundos
- Integración en todas las operaciones CRUD, login, registro y mensajería

---

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
|------------|-----------|
| Backend | Django 6.0.4 |
| Frontend | Bootstrap 5.3.3 + Bootstrap Icons 1.11.3 |
| Tipografía | Google Fonts (Inter) |
| Base de datos | SQLite3 |
| Imágenes | Pillow 12.2.0 |
| Patrón | MVT (Model - View - Template) |
| Vistas | FBV + CBV (ListView, CreateView, UpdateView, DeleteView) |
| Autenticación | Django Auth + Profile extendido |
| Idioma/Zona | es-ar / America/Argentina/Buenos_Aires |

---

## 📁 Estructura del Proyecto

```
Proyecto PowerFit Gym/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── mi_proyecto/              # Configuración Django
│   ├── settings.py           # MESSAGE_TAGS, MEDIA, LOGIN_* config
│   ├── urls.py               # include() de las 3 apps
│   └── wsgi/asgi.py
├── mainn/                    # App principal (CRUD de gimnasio)
│   ├── models.py             # 4 modelos: Socio, Entrenador, Rutina, Asistencia
│   ├── views.py              # FBV + 2 CBV (ListView, DeleteView con mixins)
│   ├── forms.py              # 7 formularios con widgets Bootstrap
│   ├── urls.py               # 18 rutas con nombres descriptivos
│   └── admin.py              # 4 modelos registrados
├── accounts/                 # App de autenticación y perfiles
│   ├── models.py             # Profile (avatar, bio, fecha, ciudad)
│   ├── views.py              # RegistroView, CustomLoginView, ProfileUpdateView
│   ├── forms.py              # RegistroForm, ProfileForm
│   ├── urls.py               # /cuentas/login, /registro, /perfil, /perfil/editar
│   ├── apps.py               # post_save signal para crear Profile
│   └── admin.py              # ProfileAdmin con búsqueda
├── messaging/                # App de mensajería interna
│   ├── models.py             # Mensaje (emisor, receptor, contenido, leido)
│   ├── views.py              # BandejaEntradaView, MensajeCreateView + 2 FBV
│   ├── forms.py              # MensajeForm con queryset filtrado
│   ├── urls.py               # /mensajes, /enviar, /enviados, /conversacion/<user>
│   └── admin.py              # MensajeAdmin con filtros y búsqueda
├── templates/
│   ├── base.html             # Layout + navbar + toasts + footer
│   ├── inicio.html           # Dashboard con estadísticas
│   ├── acerca_de_mi.html     # Página estática "Acerca"
│   ├── socios/               # lista, detalle, crear, upload_avatar, confirmar_eliminar
│   ├── entrenadores/         # crear, editar, lista, upload_foto, confirmar_eliminar
│   ├── rutinas/              # crear, editar, lista, confirmar_eliminar
│   ├── asistencias/          # crear, lista, confirmar_eliminar
│   ├── accounts/             # login, registro, perfil, editar_perfil, perfil_publico
│   └── messaging/            # bandeja, enviar, enviados, conversacion
└── media/                    # Avatares, fotos y archivos subidos
```

---

## 🎨 Diseño UI/UX

- **Dark mode** profesional con paleta personalizada (CSS variables)
- Navbar sticky con glassmorphism (`backdrop-filter: blur`) y dropdown de usuario
- Tarjetas con hover animado y bordes con gradiente
- Badges de colores por membresía (Básica / Premium / VIP) y turno (Mañana / Tarde / Noche)
- Animaciones `fadeInUp` escalonadas en listas
- Scrollbar personalizado
- Empty states descriptivos con CTAs
- Burbujas de chat diferenciadas (emisor / receptor) en la mensajería
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
| `/acerca-de-mi/` | Página "Acerca" del proyecto |
| `/socios/` | Gestión de socios |
| `/socios/<id>/` | **Detalle** del socio (rutinas + asistencias) |
| `/entrenadores/` | Gestión de entrenadores |
| `/rutinas/` | Gestión de rutinas + buscador (CBV) |
| `/asistencias/` | Registro de asistencias (requiere login) |
| `/asistencias/checkin/<id>/` | Check-in rápido |
| `/cuentas/login/` | Iniciar sesión |
| `/cuentas/registro/` | Registrarse |
| `/cuentas/perfil/` | Mi perfil (requiere login) |
| `/cuentas/perfil/editar/` | Editar mi perfil (CBV) |
| `/cuentas/perfil/<username>/` | Perfil público de un usuario |
| `/mensajes/` | Bandeja de entrada (CBV) |
| `/mensajes/enviar/` | Enviar mensaje (CBV) |
| `/mensajes/enviados/` | Mensajes enviados (FBV) |
| `/mensajes/conversacion/<username>/` | Conversación 1-a-1 |
| `/admin/` | Panel de administración Django |

---

## 💡 Aspectos Técnicos Destacados

- ✅ Patrón **MTV** de Django aplicado correctamente
- ✅ Combinación de **FBV** y **CBV** (ListView, CreateView, UpdateView, DeleteView)
- ✅ Uso de **mixins** (`LoginRequiredMixin`, `UserPassesTestMixin`) y **decoradores** (`@login_required`, `method_decorator`)
- ✅ `select_related` / `prefetch_related` para optimizar queries
- ✅ `get_object_or_404` para manejo seguro de errores
- ✅ `Q objects` para búsquedas OR complejas
- ✅ `messages.success` / `messages.error` en todas las operaciones
- ✅ Templates con herencia (`base.html` → child templates)
- ✅ URLs RESTful con `namespace` y nombres semánticos
- ✅ Formularios `ModelForm` con validación server-side
- ✅ Autenticación completa con `Profile` extendido y `post_save` signal
- ✅ Mensajería 1-a-1 con marcado automático de leídos
- ✅ Servicio de archivos media en desarrollo (`static()`)
- ✅ Código documentado con docstrings y comentarios

---

**Versión:** 3.0.0 — Entrega Final  
**Última actualización:** 3 de junio de 2026  
**Estado:** ✅ Producción lista