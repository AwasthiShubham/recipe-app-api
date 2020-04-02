from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext as translate_func


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (translate_func('Personal Info'), {'fields': ('name', )}),
        (
            translate_func('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (translate_func('Important dates'), {'fields': ('last_login', )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
            }),
    )


admin.site.register(models.User, UserAdmin)
