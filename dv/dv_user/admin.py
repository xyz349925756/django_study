from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
# Register your models here.
from dv_user import models


class UserAdmin(DjangoUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('username', 'password1', 'password2', 'email', 'is_staff', 'is_active', 'phone', 'avatar'),
            },
        ),
    )

    list_display = ('username', 'phone', 'avatar', 'last_login', 'is_staff', 'is_active', 'is_superuser')


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Books)
