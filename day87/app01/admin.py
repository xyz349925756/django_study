from django.contrib import admin

# Register your models here.

from . import models
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


class UserAdmin(DjangoUserAdmin):
    # 定义用户可操作字段filed
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'phone_num', 'groups', 'user_permissions'),
        }),
    )
    # 展示用户呈现的字段fields
    list_display = ('username', 'phone_num', 'is_staff', 'is_active', 'is_superuser')


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Book)
admin.site.register(models.Car)
