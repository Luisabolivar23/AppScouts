from datetime import date

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser


class UsersModel(AbstractUser):
    # generos
    MAN = 'M'
    WOMAN = 'W'
    OTHER = 'O'

    # roles
    SUPERUSER = 'SU'
    EDITOR = 'ED'
    USUARIO = 'US'
    USUARIO_CON_PRIVILEGIOS = 'UP'

    # tipo de documento
    CEDULA_DE_CIUDANIA = 'CC'
    CEDULA_DE_EXTRANJERIA = 'CE'
    PERMISO_ESPECIAL_DE_PERMANENCIA = 'PEP'
    REGISTRO_CIVIL = 'RC'
    TARJETA_DE_IDENTIDAD = 'TI'
    VISA = 'V'
    PASAPORTE = 'PP'

    DOCUMENT_TYPE = [
        (CEDULA_DE_CIUDANIA, 'Cédula de ciudadania'),
        (CEDULA_DE_EXTRANJERIA, 'Cédula de extranjería'),
        (PERMISO_ESPECIAL_DE_PERMANENCIA, 'Permiso especial de permanencia'),
        (REGISTRO_CIVIL, 'Registro Civil'),
        (TARJETA_DE_IDENTIDAD, 'Tarjeta de Identidad'),
        (VISA, 'Visa'),
        (PASAPORTE, 'Pasaporte'),
    ]

    ROLE_IN_CHOICES = [
        (SUPERUSER, 'Administrador'),
        (EDITOR, 'Editor'),
        (USUARIO, 'Usuario'),
        (USUARIO_CON_PRIVILEGIOS, 'Usuario con privilegios'),
    ]

    GENDER_IN_CHOICES = [
        (MAN, 'Hombre'),
        (WOMAN, 'Mujer'),
        (OTHER, 'Otro')
    ]

    full_name = models.CharField(
        'Nombre(s) y Apellido(s)',
        max_length=300,
        default='',
    )

    first_name = models.CharField(
        "Nombre(s)",
        max_length=150
    )

    last_name = models.CharField(
        "Apellido(s)",
        max_length=150
    )

    birthday = models.DateField(
        'Fecha de nacimiento',
        default=timezone.now
    )

    age = models.IntegerField(
        'Edad',
        default=0
    )

    email = models.EmailField(
        'Correo electrónico',
        unique=True,
    )

    document_type = models.CharField(
        "Tipo de documento",
        choices=DOCUMENT_TYPE,
        max_length=50,
        default=CEDULA_DE_CIUDANIA
    )
    
    document_number = models.CharField(
        "Número de documento",
        max_length=100
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
    )

    role = models.CharField(
        "Rol",
        max_length=20,
        choices=ROLE_IN_CHOICES,
        default=USUARIO,
    )

    gender = models.CharField(
        "Género",
        choices=GENDER_IN_CHOICES,
        max_length=20,
        default=OTHER,
    )

    is_active = models.BooleanField(
        'Es una persona activa',
        default=True,
    )

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthday', 'username']

    def save(self, *args, **kwargs):

        self.full_name = f"{self.first_name} {self.last_name}"

        self.age = date.today().year - self.birthday.year - (
            (
                date.today().month, date.today().day
            ) < (
                self.birthday.month, self.birthday.day
            )
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'apps_autenticacion_users_model'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['order', 'id', 'last_name', 'first_name']
