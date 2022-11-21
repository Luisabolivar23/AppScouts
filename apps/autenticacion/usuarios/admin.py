from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.autenticacion.usuarios.models import UsersModel


@admin.register(UsersModel)
class UserAdmin(UserAdmin):
    list_display = (
        "full_name",
        "email",
        "is_staff",
        "age"
    )

    fieldsets = (
        (
            "Datos de Usuario",
            {
                "fields": (
                    "username",
                    "password",
                )
            }
        ),
        (
            "Información Personal",
            {
                "fields": (
                    "full_name",
                    "first_name",
                    "last_name",
                    "email",
                    "birthday",
                    "gender"
                )
            }
        ),
        (
            "Permisos",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "role",
                    "order"
                ),
            },
        ),
        (
            "Fechas",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                    "age"
                )
            }
        ),
    )

    ordering = (
        "id",
        "email",
        "first_name",
        "last_name"
    )

    readonly_fields = (
        "full_name",
        "last_login",
        "date_joined",
        "age"
    )
