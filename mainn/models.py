from django.db import models


class Socio(models.Model):
    """Modelo que representa a un socio del gimnasio PowerFit."""

    TIPO_MEMBRESIA_CHOICES = [
        ('basica', 'Básica'),
        ('premium', 'Premium'),
        ('vip', 'VIP'),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    tipo_membresia = models.CharField(
        max_length=10,
        choices=TIPO_MEMBRESIA_CHOICES,
        default='basica',
    )
    fecha_inscripcion = models.DateField(auto_now_add=True)
    avatar = models.ImageField(
        upload_to='avatares/',
        blank=True,
        null=True,
        verbose_name='Avatar',
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"


class Entrenador(models.Model):
    """Modelo que representa a un entrenador del gimnasio PowerFit."""

    TURNO_CHOICES = [
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
        ('noche', 'Noche'),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    email = models.EmailField()
    turno = models.CharField(
        max_length=10,
        choices=TURNO_CHOICES,
        default='mañana',
    )
    foto = models.ImageField(
        upload_to='entrenadores/',
        blank=True,
        null=True,
        verbose_name='Foto',
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"

    class Meta:
        verbose_name = "Entrenador"
        verbose_name_plural = "Entrenadores"


class Rutina(models.Model):
    """Modelo que representa una rutina de entrenamiento."""

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_semanas = models.PositiveIntegerField(help_text="Duración en semanas")
    entrenador = models.ForeignKey(
        Entrenador,
        on_delete=models.CASCADE,
        related_name='rutinas',
    )
    socios = models.ManyToManyField(
        Socio,
        related_name='rutinas',
        blank=True,
    )

    def __str__(self):
        return f"{self.nombre} ({self.duracion_semanas} semanas)"

    class Meta:
        verbose_name = "Rutina"
        verbose_name_plural = "Rutinas"


class Asistencia(models.Model):
    """Modelo que representa la asistencia de un socio al gimnasio."""

    TIPO_ACTIVIDAD_CHOICES = [
        ('musculacion', 'Musculación'),
        ('cardio', 'Cardio'),
        ('crossfit', 'CrossFit'),
        ('yoga', 'Yoga'),
        ('spinning', 'Spinning'),
        ('funcional', 'Funcional'),
    ]

    socio = models.ForeignKey(
        Socio,
        on_delete=models.CASCADE,
        related_name='asistencias',
    )
    fecha = models.DateTimeField(auto_now_add=True)
    tipo_actividad = models.CharField(
        max_length=20,
        choices=TIPO_ACTIVIDAD_CHOICES,
        default='musculacion',
    )

    def __str__(self):
        return f"{self.socio} - {self.get_tipo_actividad_display()} ({self.fecha.strftime('%d/%m/%Y %H:%M')})"

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        ordering = ['-fecha']
