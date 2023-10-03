from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'father_name', 'dob', 'phone', 'mobile', 'address', 'is_teacher', 'is_principal', 'is_staff', 'is_active')
    list_filter = ('is_teacher', 'is_principal', 'is_staff', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'father_name', 'dob', 'phone', 'mobile', 'address')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_teacher', 'is_principal', 'groups')}),
        ('Profile Picture', {'fields': ('profile_picture',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'father_name', 'dob', 'phone', 'mobile', 'address', 'is_staff', 'is_active', 'is_teacher', 'is_principal', 'groups', 'profile_picture'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name', 'address', 'mobile')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
