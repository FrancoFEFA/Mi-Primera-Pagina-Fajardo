# Guía para iniciar un proyecto Django

## 1. Preparación del entorno

### Crear la estructura del proyecto
1. Crea una carpeta para tu proyecto
2. Abre la carpeta en VSCode
3. Crea un archivo `.gitignore` con las configuraciones para `visualstudiocode`, `python` y `django` (puedes generarlo en [gitignore.io](https://gitignore.io))

### Configurar el entorno virtual
4. Crea el entorno virtual:
   ```shell
   python -m venv .venv
   ```
5. Agrega `.venv/` al archivo `.gitignore`

### Inicializar el repositorio Git
6. Inicializa Git:
   ```shell
   git init
   ```
7. Realiza el primer commit:
   ```shell
   git add .
   git commit -m "Initial commit"
   ```
8. Conecta con GitHub (u otro repositorio remoto)
9. Haz el primer push

## 2. Instalación y configuración de Django

### Activar el entorno virtual
10. Activa el entorno virtual según tu sistema operativo:

    **Windows (PowerShell):**
    ```shell
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    .\.venv\Scripts\Activate.ps1
    ```

    **Windows (CMD):**
    ```shell
    .venv\Scripts\activate
    ```

    **Linux/Mac:**
    ```shell
    source .venv/bin/activate
    ```

    Para desactivar: `deactivate`

### Instalar Django
11. Instala Django usando pip:
    ```shell
    pip install Django
    ```

12. Crea el archivo `requirements.txt`:
    ```shell
    pip freeze > requirements.txt
    ```
    > **Nota:** Repite este comando cada vez que instales nuevos paquetes.

### Crear el proyecto Django
13. Crea el proyecto Django en el directorio actual:
    ```shell
    django-admin startproject mi_proyecto .
    ```
    > **Importante:** El punto `.` al final evita que se cree una carpeta adicional.

14. Verifica que funciona:
    ```shell
    python manage.py migrate
    python manage.py runserver
    ```

## 3. Configuración de la aplicación principal

### Crear la app
15. Crea tu app principal:
    ```shell
    python manage.py startapp nombre_app
    ```

16. Registra la app en `settings.py`:
    - Abre `settings.py`
    - Agrega `nombre_app` a la lista `INSTALLED_APPS`

17. Configura las URLs de la app:
    - Crea un archivo `urls.py` dentro de tu app
    - En el `urls.py` principal, agrega:
      ```python
      from django.urls import include, path

      urlpatterns = [
          path('ruta/', include('nombre_app.urls')),
      ]
      ```

### Configurar templates
18. Configura la carpeta de templates en `settings.py`:
    ```python
    TEMPLATES = [
        {
            'DIRS': [BASE_DIR / 'templates'],
        },
    ]
    ```

19. Crea la carpeta `templates` en la raíz del proyecto (al mismo nivel que `manage.py`)

## 4. Configuración del administrador

20. Crea un superusuario:
    ```shell
    python manage.py createsuperuser
    ```
    > **Nota:** La contraseña no se muestra mientras escribes, pero se está ingresando correctamente.

21. Accede al panel de administración en: `http://127.0.0.1:8000/admin`

## 5. Crear vistas

22. Para cada vista:
    - Define el path en `urls.py` de tu app
    - Crea la función vista en `views.py` de tu app
    - Crea el template HTML en la carpeta `templates`
    - Agrega enlaces (`<a>`) hacia las rutas correspondientes

## 6. Crear modelos

23. Define el modelo en `models.py`:
    ```python
    from django.db import models

    class MiModelo(models.Model):
        nombre = models.CharField(max_length=100)
        # más campos...
    ```

24. Genera y aplica las migraciones:
    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

25. Registra el modelo en `admin.py`:
    ```python
    from django.contrib import admin
    from .models import MiModelo

    admin.site.register(MiModelo)
    ```

26. Importa el modelo en `views.py` para usarlo en tus vistas

## 7. Crear formularios

27. Crea el archivo `forms.py` en tu app

28. Define el formulario:
    ```python
    from django import forms

    class MiFormulario(forms.Form):
        campo = forms.CharField(max_length=100)
    ```

29. Importa y usa el formulario en `views.py`

---

## Notas importantes

- **Entorno virtual:** Si no usas entorno virtual, omite los pasos relacionados
- **requirements.txt:** Actualízalo después de cada instalación de paquetes
- **Migraciones:** Ejecuta `makemigrations` y `migrate` cada vez que modifiques modelos
- **URLs y vistas:** Asegúrate de que las URLs coincidan correctamente con tus vistas