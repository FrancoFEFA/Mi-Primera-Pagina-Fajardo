# PowerFit - Sistema de Gestión de Gimnasio

Sistema web desarrollado con **Django** para la gestión completa de un gimnasio, permitiendo administrar socios, entrenadores, rutinas de entrenamiento y registro de asistencias.

---

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
- [Guía de Pruebas](#guía-de-pruebas)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Documentación de Funcionalidades](#documentación-de-funcionalidades)
- [Panel de Administración](#panel-de-administración)

---

## 📖 Descripción

PowerFit es una aplicación web diseñada para simplificar la gestión administrativa de un gimnasio. Permite registrar y administrar socios con diferentes tipos de membresía, gestionar entrenadores especializados, crear rutinas personalizadas y llevar un registro de asistencias.

**Stack Tecnológico:**
- **Backend:** Django 6.0.4
- **Base de Datos:** SQLite3
- **Frontend:** HTML5 + Bootstrap (CSS)
- **Lenguaje:** Python 3.x

---

## ✨ Características

### 🧑‍💼 Gestión de Socios
- Registrar nuevos socios
- Asignar tipos de membresía (Básica, Premium, VIP)
- Listar todos los socios registrados
- Ver información detallada: nombre, apellido, email, tipo de membresía
- Registro automático de fecha de inscripción

### 👨‍🏫 Gestión de Entrenadores
- Registrar entrenadores con especialidades
- Asignar turnos de trabajo (Mañana, Tarde, Noche)
- Listar todos los entrenadores
- Registrar email de contacto

### 💪 Gestión de Rutinas
- Crear rutinas de entrenamiento personalizadas
- Asignar rutinas a entrenadores
- Vincular rutinas a socios
- Especificar duración de las rutinas (en semanas)
- **Búsqueda avanzada** por nombre de rutina o especialidad del entrenador

### 📊 Registro de Asistencias
- Registrar asistencias de socios
- Categorizar por tipo de actividad (Musculación, Cardio, CrossFit, Yoga, Spinning, Funcional)
- Listar historial de asistencias ordenado por fecha
- Visualizar las últimas 5 asistencias en la página de inicio

### 📈 Panel de Estadísticas
- Página de inicio con estadísticas generales:
  - Total de socios registrados
  - Total de entrenadores
  - Total de rutinas
  - Total de asistencias
  - Últimas asistencias registradas

---

## 🔧 Requisitos

- **Python 3.8+**
- **pip** (gestor de paquetes de Python)
- **Git** (opcional, para control de versiones)

### Dependencias del Proyecto
Se encuentran en `requirements.txt`:
```
Django==6.0.4
asgiref==3.11.1
sqlparse==0.5.5
tzdata==2026.1
```

---

## 📦 Instalación

### Paso 1: Clonar o Descargar el Repositorio

```bash
# Si clona desde GitHub
git clone https://github.com/tu-usuario/segunda-entrega-noop.git
cd SegundaEntreganoop
```

### Paso 2: Crear y Activar el Entorno Virtual

**En Windows (PowerShell):**
```powershell
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\.venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

**En Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Paso 3: Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Paso 4: Realizar Migraciones de Base de Datos

```bash
cd mi_proyecto
python manage.py migrate
```

### Paso 5: Crear Superusuario (Administrador)

```bash
python manage.py createsuperuser
```
Se te pedirá ingresar:
- Nombre de usuario
- Email
- Contraseña (no se mostrará mientras escribes por seguridad)
- Confirmación de contraseña

---

## 🚀 Ejecución

### Iniciar el Servidor de Desarrollo

```bash
python manage.py runserver
```

**Salida esperada:**
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Luego abre tu navegador y accede a:
- **URL Principal:** `http://127.0.0.1:8000/`
- **Panel de Administración:** `http://127.0.0.1:8000/admin/`

---

## 🧪 Guía de Pruebas

### Recomendaciones Previas
1. Asegúrate de que el servidor esté ejecutándose
2. Crea un superusuario siguiendo los pasos de instalación
3. Recomendamos probar en el siguiente orden para una mejor experiencia

---

### 📌 Orden de Pruebas Recomendado

#### **1️⃣ Panel de Administración (Primera Vez)**

1. Accede a: `http://127.0.0.1:8000/admin/`
2. Inicia sesión con las credenciales del superusuario que creaste
3. Explora las secciones:
   - **Socios** - Ver tabla vacía inicialmente
   - **Entrenadores** - Ver tabla vacía
   - **Rutinas** - Ver tabla vacía
   - **Asistencias** - Ver tabla vacía

✅ **Resultado esperado:** Deberías ver el panel de administración de Django con acceso a todas las tablas.

---

#### **2️⃣ Crear Entrenadores (Paso Previo)**

Los entrenadores deben existir antes de crear rutinas.

**Opción A: A través del Panel de Administración**
1. Ve a: `http://127.0.0.1:8000/admin/mainn/entrenador/add/`
2. Completa el formulario:
   - Nombre: Juan
   - Apellido: Pérez
   - Especialidad: Musculación
   - Email: juan@gym.com
   - Turno: Mañana
3. Haz clic en "Guardar"

**Opción B: A través de la Interfaz Web**
1. Ve a: `http://127.0.0.1:8000/entrenadores/crear/`
2. Completa el formulario
3. Haz clic en "Guardar"

✅ **Resultado esperado:** El entrenador se guarda y puedes verlo listado.

---

#### **3️⃣ Crear Socios**

**Opción A: Desde la Interfaz Web**
1. Ve a: `http://127.0.0.1:8000/socios/crear/`
2. Completa el formulario:
   - Nombre: Carlos
   - Apellido: García
   - Email: carlos@email.com
   - Tipo de Membresía: Premium
3. Haz clic en "Guardar"

**Opción B: Desde el Panel de Administración**
1. Ve a: `http://127.0.0.1:8000/admin/mainn/socio/add/`
2. Completa el formulario similar

Repite el proceso para crear al menos 3-4 socios con diferentes tipos de membresía.

✅ **Resultado esperado:** Los socios aparecen en la lista en `http://127.0.0.1:8000/socios/`

---

#### **4️⃣ Crear Rutinas**

1. Ve a: `http://127.0.0.1:8000/rutinas/crear/`
2. Completa el formulario:
   - Nombre: Rutina Full Body
   - Descripción: Entrenamiento completo de cuerpo
   - Duración (semanas): 4
   - Entrenador: (Selecciona el entrenador creado)
   - Socios: (Selecciona los socios creados - puedes elegir múltiples)
3. Haz clic en "Guardar"

Crea al menos 2-3 rutinas diferentes.

✅ **Resultado esperado:** Las rutinas aparecen listadas en `http://127.0.0.1:8000/rutinas/`

---

#### **5️⃣ Probar Búsqueda de Rutinas**

1. Ve a: `http://127.0.0.1:8000/rutinas/`
2. En el buscador, prueba:
   - Buscar por nombre de rutina: "Full Body"
   - Buscar por especialidad: "Musculación"
   - Buscar texto incompleto: "rut"

✅ **Resultado esperado:** Las rutinas se filtran según los criterios de búsqueda (búsqueda insensible a mayúsculas).

---

#### **6️⃣ Registrar Asistencias**

Las asistencias se registran a través del Panel de Administración:

1. Ve a: `http://127.0.0.1:8000/admin/mainn/asistencia/add/`
2. Completa el formulario:
   - Socio: (Selecciona un socio)
   - Tipo de Actividad: Musculación
   - (La fecha se registra automáticamente con la hora actual)
3. Haz clic en "Guardar"

Registra varias asistencias para diferentes socios y actividades.

✅ **Resultado esperado:** Las asistencias aparecen en `http://127.0.0.1:8000/asistencias/` ordenadas por fecha (más recientes primero).

---

#### **7️⃣ Verificar Página de Inicio**

1. Ve a: `http://127.0.0.1:8000/`

Deberías ver:
- ✅ Estadísticas actualizadas:
  - Total de socios creados
  - Total de entrenadores
  - Total de rutinas
  - Total de asistencias
- ✅ Las últimas 5 asistencias registradas con información del socio

---

#### **8️⃣ Verificar Listados**

Prueba cada vista de listado:

1. **Socios:** `http://127.0.0.1:8000/socios/` 
   - Los socios deben aparecer ordenados alfabéticamente por apellido

2. **Entrenadores:** `http://127.0.0.1:8000/entrenadores/`
   - Los entrenadores ordenados por apellido

3. **Rutinas:** `http://127.0.0.1:8000/rutinas/`
   - Las rutinas con información del entrenador y socios asociados

4. **Asistencias:** `http://127.0.0.1:8000/asistencias/`
   - Historial completo ordenado por fecha descendente

---

## 📁 Estructura del Proyecto

```
SegundaEntreganoop/
├── README.md                          # Este archivo
├── requirements.txt                   # Dependencias del proyecto
├── pasos_django.md                    # Guía de pasos de Django (referencia)
├── .venv/                             # Entorno virtual (no incluido en git)
├── Entregas/
│   └── entrega1.md                    # Documentación de entrega anterior
└── mi_proyecto/
    ├── manage.py                      # Script de administración de Django
    ├── db.sqlite3                     # Base de datos SQLite
    ├── mi_proyecto/                   # Configuración principal del proyecto
    │   ├── __init__.py
    │   ├── settings.py                # ⚙️ Configuración de Django
    │   ├── urls.py                    # Rutas principales del proyecto
    │   ├── asgi.py
    │   └── wsgi.py
    ├── mainn/                         # Aplicación principal
    │   ├── __init__.py
    │   ├── models.py                  # 📊 Modelos: Socio, Entrenador, Rutina, Asistencia
    │   ├── views.py                   # 👁️ Vistas (lógica de las páginas)
    │   ├── urls.py                    # Rutas de la aplicación mainn
    │   ├── forms.py                   # 📝 Formularios
    │   ├── admin.py                   # ⚙️ Configuración del panel de administración
    │   ├── apps.py
    │   ├── tests.py
    │   └── migrations/                # 🗄️ Migraciones de base de datos
    │       ├── __init__.py
    │       ├── 0001_initial.py
    │       ├── 0002_persona_nacimiento.py
    │       └── 0003_asistencia_entrenador_rutina_socio_delete_persona_and_more.py
    └── templates/                     # 🎨 Plantillas HTML
        ├── base.html                  # Template base con navegación
        ├── inicio.html                # Página de inicio (estadísticas)
        ├── socios/
        │   ├── crear.html             # Formulario para crear socio
        │   └── lista.html             # Listado de socios
        ├── entrenadores/
        │   ├── crear.html             # Formulario para crear entrenador
        │   └── lista.html             # Listado de entrenadores
        ├── rutinas/
        │   ├── crear.html             # Formulario para crear rutina
        │   └── lista.html             # Listado de rutinas con búsqueda
        └── asistencias/
            └── lista.html             # Listado de asistencias
```

---

## 🗄️ Documentación de Funcionalidades

### Archivos Clave por Funcionalidad

#### **👥 Gestión de Socios**
| Archivo | Línea | Descripción |
|---------|-------|-------------|
| [mainn/models.py](mi_proyecto/mainn/models.py) | 4-23 | Modelo `Socio` con tipos de membresía |
| [mainn/views.py](mi_proyecto/mainn/views.py) | 16-27 | Vistas: `lista_socios()`, `crear_socio()` |
| [mainn/forms.py](mi_proyecto/mainn/forms.py) | 1-34 | Formulario `SocioForm` |
| [mainn/urls.py](mi_proyecto/mainn/urls.py) | 6-7 | Rutas: `/socios/` y `/socios/crear/` |
| [templates/socios/](mi_proyecto/templates/socios/) | - | Templates para crear y listar |

#### **👨‍🏫 Gestión de Entrenadores**
| Archivo | Línea | Descripción |
|---------|-------|-------------|
| [mainn/models.py](mi_proyecto/mainn/models.py) | 26-47 | Modelo `Entrenador` con especialidades |
| [mainn/views.py](mi_proyecto/mainn/views.py) | 31-42 | Vistas: `lista_entrenadores()`, `crear_entrenador()` |
| [mainn/forms.py](mi_proyecto/mainn/forms.py) | 37-76 | Formulario `EntrenadorForm` |
| [mainn/urls.py](mi_proyecto/mainn/urls.py) | 10-11 | Rutas: `/entrenadores/` y `/entrenadores/crear/` |

#### **💪 Gestión de Rutinas**
| Archivo | Línea | Descripción |
|---------|-------|-------------|
| [mainn/models.py](mi_proyecto/mainn/models.py) | 50-72 | Modelo `Rutina` con búsqueda |
| [mainn/views.py](mi_proyecto/mainn/views.py) | 46-68 | Vistas con búsqueda usando `Q` de Django |
| [mainn/forms.py](mi_proyecto/mainn/forms.py) | 79-117 | Formulario `RutinaForm` |
| [mainn/urls.py](mi_proyecto/mainn/urls.py) | 14-15 | Rutas: `/rutinas/` y `/rutinas/crear/` |

#### **📊 Registro de Asistencias**
| Archivo | Línea | Descripción |
|---------|-------|-------------|
| [mainn/models.py](mi_proyecto/mainn/models.py) | 75-96 | Modelo `Asistencia` |
| [mainn/views.py](mi_proyecto/mainn/views.py) | 72-75 | Vista: `lista_asistencias()` |
| [mainn/urls.py](mi_proyecto/mainn/urls.py) | 18 | Ruta: `/asistencias/` |

#### **🔍 Búsqueda Avanzada**
- **Ubicación:** [mainn/views.py](mi_proyecto/mainn/views.py#L46-L68) - Función `lista_rutinas()`
- **Tecnología:** Django ORM con `Q` (permite búsquedas OR)
- **Campos:** Nombre de rutina + Especialidad del entrenador
- **Tipo:** Búsqueda insensible a mayúsculas (`icontains`)

---

## 🔐 Panel de Administración

### Acceso

```
URL: http://127.0.0.1:8000/admin/
Usuario: (El que creaste con createsuperuser)
```

### Modelos Disponibles en Admin

1. **Socios**
   - Ver todos los socios
   - Crear nuevos socios
   - Editar información
   - Eliminar socios

2. **Entrenadores**
   - Gestionar entrenadores
   - Asignar especialidades y turnos

3. **Rutinas**
   - Crear y editar rutinas
   - Asignar a socios y entrenadores

4. **Asistencias**
   - Registrar asistencias
   - Verificar historiales

### Configuración Admin
Archivo: [mainn/admin.py](mi_proyecto/mainn/admin.py)

Todos los modelos están registrados usando:
```python
admin.site.register([Socio, Entrenador, Rutina, Asistencia])
```

---

## 🌐 Rutas Disponibles

### Navegación Principal

| Ruta | Descripción | Método |
|------|-------------|--------|
| `/` | Página de inicio con estadísticas | GET |
| `/socios/` | Listado de socios | GET |
| `/socios/crear/` | Crear nuevo socio | GET, POST |
| `/entrenadores/` | Listado de entrenadores | GET |
| `/entrenadores/crear/` | Crear nuevo entrenador | GET, POST |
| `/rutinas/` | Listado de rutinas (con búsqueda) | GET |
| `/rutinas/crear/` | Crear nueva rutina | GET, POST |
| `/asistencias/` | Listado de asistencias | GET |
| `/admin/` | Panel de administración | GET, POST |

---

## 💾 Modelos de Base de Datos

### Socio
```python
- nombre (CharField, 50)
- apellido (CharField, 50)
- email (EmailField)
- tipo_membresia (Choices: basica, premium, vip)
- fecha_inscripcion (DateField, automática)
```

### Entrenador
```python
- nombre (CharField, 50)
- apellido (CharField, 50)
- especialidad (CharField, 100)
- email (EmailField)
- turno (Choices: mañana, tarde, noche)
- rutinas (Relación inversa desde Rutina)
```

### Rutina
```python
- nombre (CharField, 100)
- descripcion (TextField)
- duracion_semanas (PositiveIntegerField)
- entrenador (ForeignKey → Entrenador)
- socios (ManyToMany → Socio)
```

### Asistencia
```python
- socio (ForeignKey → Socio)
- fecha (DateTimeField, automática)
- tipo_actividad (Choices: musculacion, cardio, crossfit, yoga, spinning, funcional)
```

---

## 📤 Subir a GitHub

### Paso 1: Preparar el Repositorio Local

```bash
# Inicializar git si no está inicializado
git init

# Crear archivo .gitignore (si no existe)
# Debe incluir:
# .venv/
# *.pyc
# __pycache__/
# *.sqlite3
# .DS_Store
```

### Paso 2: Agregar Archivos al Staging

```bash
git add .
```

### Paso 3: Hacer el Primer Commit

```bash
git commit -m "Proyecto PowerFit - Sistema de gestión de gimnasio"
```

### Paso 4: Crear Repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre: `powerfit-gym` o `segunda-entrega-noop`
3. Descripción: "Sistema web para gestión de gimnasio con Django"
4. Elige entre público o privado
5. NO inicialices con README (ya tenemos uno)
6. Haz clic en "Create repository"

### Paso 5: Conectar Repositorio Local con GitHub

```bash
git remote add origin https://github.com/tu-usuario/powerfit-gym.git
git branch -M main
git push -u origin main
```

### Paso 6: Verificar

Abre https://github.com/tu-usuario/powerfit-gym en tu navegador para verificar que todo se subió correctamente.

---

## 🔄 Comandos Útiles de Django

### Migraciones

```bash
# Ver estado de migraciones
python manage.py showmigrations

# Hacer migraciones después de cambios en modelos
python manage.py makemigrations

# Aplicar migraciones a la BD
python manage.py migrate

# Revertir a una migración anterior
python manage.py migrate mainn 0001
```

### Base de Datos

```bash
# Crear superusuario
python manage.py createsuperuser

# Acceder a la shell de Django
python manage.py shell

# Generar datos de prueba (si existe fixture)
python manage.py loaddata fixture_name
```

### Otros

```bash
# Ver información del proyecto
python manage.py help

# Ejecutar pruebas
python manage.py test

# Recopilar archivos estáticos
python manage.py collectstatic
```

---

## ✅ Checklist de Verificación

Antes de entregar, verifica que:

- ✅ El servidor corre sin errores: `python manage.py runserver`
- ✅ Todas las migraciones están aplicadas: `python manage.py migrate`
- ✅ Superusuario creado correctamente
- ✅ Panel de admin accesible: `http://127.0.0.1:8000/admin/`
- ✅ Página de inicio muestra estadísticas
- ✅ Puedes crear socios
- ✅ Puedes crear entrenadores
- ✅ Puedes crear rutinas
- ✅ La búsqueda de rutinas funciona
- ✅ Puedes registrar asistencias
- ✅ README.md presente en la raíz
- ✅ requirements.txt actualizado
- ✅ .gitignore correctamente configurado
- ✅ Repositorio subido a GitHub

---

## 📞 Soporte

Para problemas comunes:

### Error: "No module named 'django'"
```bash
pip install -r requirements.txt
```

### Error: "Table doesn't exist"
```bash
python manage.py migrate
```

### Error: "Permission denied" en PowerShell
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### El servidor no se ejecuta
- Verifica que estés en la carpeta correcta: `mi_proyecto`
- Verifica que el entorno virtual esté activado
- Intenta otro puerto: `python manage.py runserver 8001`

---

## 📝 Notas

- La base de datos SQLite (`db.sqlite3`) se crea automáticamente en la primera migración
- Los cambios en modelos requieren `makemigrations` seguido de `migrate`
- La búsqueda es insensible a mayúsculas/minúsculas
- La fecha de asistencias se registra automáticamente
- Las estadísticas de la página de inicio se actualizan en tiempo real

---

## 📄 Licencia

Este proyecto fue desarrollado como parte de una entrega educativa.

---

**Última actualización:** 30 de abril de 2026

**Versión:** 1.0
