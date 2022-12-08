from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "first_name", "last_name", "is_superuser", 'created_at']
    list_filter = ['is_superuser']
    fieldsets = (
        ('Account', {'fields': ('username', 'email', 'phone', 'password')}),
        ('Personal info', {'fields': ('first_name', 'middle_name', 'last_name', 'birthdate',)}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )

    add_fieldsets = (
        ('Account', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2')
        }),
        ('Personal info', {
            'classes': ('wide',),
            'fields': ('first_name', 'middle_name', 'last_name', 'birthdate',)
        }),
        ('Permissions', {'fields': ('is_superuser',)}),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('first_name', 'last_name', 'username', 'phone', 'birthdate', 'email',)
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
