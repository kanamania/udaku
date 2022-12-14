from datetime import datetime

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html

from .forms import *
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "first_name", "last_name", "is_superuser", 'created_at', 'status', 'show_actions']
    list_filter = ['is_superuser']
    fieldsets = (
        ('Account', {'fields': ('username', 'email', 'phone', 'password', 'status')}),
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

    def show_name(self, obj):
        url = reverse('%s_%s_detail' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html("<a href='{url}'>{name}</a>", url=url, name=obj.username)
    show_name.short_description = "Username"

    def show_actions(self, obj):
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        delete_url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        history_url = reverse('admin:%s_%s_history' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html(f"<a href='{edit_url}'><i class='fa fa-edit'></i></a><a class='text-danger mr-2 ml-2' href='{delete_url}'><i class='fa fa-trash'></i></a><a class='text-black-50' href='{history_url}'><i class='fa fa-clock'></i></a>", edit_url=edit_url, delete_url=delete_url, history_url=history_url)
    show_actions.short_description = "Actions"

    def status(self, obj):
        return 'Inactive' if obj.deleted_at else 'Active'

    def save_model(self, request, obj, form, change):
        if change:
            obj.modifier = request.user
        else:
            obj.creator = request.user
        obj.deleted_at = None if request.POST['status'] != '1' else datetime.now()
        super().save_model(request, obj, form, change)


class CategoryAdmin(ModelAdmin):
    add_form = CategoryCreationForm
    form = CategoryChangeForm
    model = Category
    list_display = ["show_name", "description", "creator", 'created_at', 'status', 'show_actions']
    search_fields = ('name', 'description')
    ordering = ('name',)
    filter_horizontal = ()

    def show_name(self, obj):
        url = reverse('%s_%s_detail' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html("<a href='{url}'>{name}</a>", url=url, name=obj.name)
    show_name.short_description = "Name"

    def show_actions(self, obj):
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        delete_url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        history_url = reverse('admin:%s_%s_history' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html(f"<a href='{edit_url}'><i class='fa fa-edit'></i></a><a class='text-danger mr-2 ml-2' href='{delete_url}'><i class='fa fa-trash'></i></a><a class='text-black-50' href='{history_url}'><i class='fa fa-clock'></i></a>", edit_url=edit_url, delete_url=delete_url, history_url=history_url)
    show_actions.short_description = "Actions"

    def status(self, obj):
        return 'Inactive' if obj.deleted_at else 'Active'

    def save_model(self, request, obj, form, change):
        if change:
            obj.modifier = request.user
        else:
            obj.creator = request.user
        obj.deleted_at = None if request.POST['status'] != '1' else datetime.now()
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.deleted_at = datetime.now()
        obj.save()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)




class RegionAdmin(ModelAdmin):
    add_form = RegionCreationForm
    form = RegionChangeForm
    model = Region
    list_display = ["show_name", "creator", 'created_at', 'status', 'show_actions']
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ()

    def show_name(self, obj):
        url = reverse('%s_%s_detail' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html("<a href='{url}'>{name}</a>", url=url, name=obj.name)
    show_name.short_description = "Name"

    def show_actions(self, obj):
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        delete_url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        history_url = reverse('admin:%s_%s_history' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html(f"<a href='{edit_url}'><i class='fa fa-edit'></i></a><a class='text-danger mr-2 ml-2' href='{delete_url}'><i class='fa fa-trash'></i></a><a class='text-black-50' href='{history_url}'><i class='fa fa-clock'></i></a>", edit_url=edit_url, delete_url=delete_url, history_url=history_url)
    show_actions.short_description = "Actions"

    def status(self, obj):
        return 'Inactive' if obj.deleted_at else 'Active'

    def save_model(self, request, obj, form, change):
        if change:
            obj.modifier = request.user
        else:
            obj.creator = request.user
        obj.deleted_at = None if request.POST['status'] != '1' else datetime.now()
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.deleted_at = datetime.now()
        obj.save()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)


class DistrictAdmin(ModelAdmin):
    MY_CHOICES = [(None, 'Active'), (1, 'Inactive')]
    add_form = DistrictCreationForm
    form = DistrictChangeForm
    model = District
    list_display = ["show_name", "region", "creator", 'created_at', 'status', 'show_actions']
    list_filter = ['region']
    search_fields = ('name',)
    ordering = ('name', 'region', 'created_at')
    filter_horizontal = ()

    def show_name(self, obj):
        url = reverse('%s_%s_detail' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html("<a href='{url}'>{name}</a>", url=url, name=obj.name)
    show_name.short_description = "Name"

    def show_actions(self, obj):
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        delete_url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        history_url = reverse('admin:%s_%s_history' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html(f"<a href='{edit_url}'><i class='fa fa-edit'></i></a><a class='text-danger mr-2 ml-2' href='{delete_url}'><i class='fa fa-trash'></i></a><a class='text-black-50' href='{history_url}'><i class='fa fa-clock'></i></a>", edit_url=edit_url, delete_url=delete_url, history_url=history_url)
    show_actions.short_description = "Actions"

    def status(self, obj):
        return 'Inactive' if obj.deleted_at else 'Active'

    def save_model(self, request, obj, form, change):
        if change:
            obj.modifier = request.user
        else:
            obj.creator = request.user
        obj.deleted_at = None if request.POST['status'] != '1' else datetime.now()
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.deleted_at = datetime.now()
        obj.save()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)


class LogAdmin(ModelAdmin):
    model = Log
    list_display = ["tag", "description", 'created_at', 'status']
    list_filter = ['tag']
    search_fields = ('tag', 'description')
    ordering = ('tag', 'description')
    filter_horizontal = ()
    readonly_fields = ["status"]

    def status(self, obj):
        return 'Inactive' if obj.deleted_at else 'Active'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.creator = request.user
        obj.deleted_at = None if request.POST['status'] != '1' else datetime.now()
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.modifier = request.user
        obj.save()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)


class SettingAdmin(ModelAdmin):
    add_form = SettingCreationForm
    form = SettingChangeForm
    model = Setting
    list_display = ["category", "tag", "description", "current_value", "creator", 'updated_at', 'status', 'show_actions']
    list_filter = ['category']

    search_fields = ('tag', 'category', 'description')
    ordering = ('category', 'tag', 'description')
    filter_horizontal = ()
    readonly_fields = ["status"]

    def show_actions(self, obj):
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        delete_url = reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        history_url = reverse('admin:%s_%s_history' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html(f"<a href='{edit_url}'><i class='fa fa-edit'></i></a><a class='text-danger mr-2 ml-2' href='{delete_url}'><i class='fa fa-trash'></i></a><a class='text-black-50' href='{history_url}'><i class='fa fa-clock'></i></a>", edit_url=edit_url, delete_url=delete_url, history_url=history_url)
    show_actions.short_description = "Actions"

    def status(self, obj):
        return 'Inactive' if obj.deleted_at else 'Active'

    def save_model(self, request, obj, form, change):
        if change:
            obj.modifier = request.user
        else:
            obj.creator = request.user
        obj.deleted_at = None if request.POST['status'] != '1' else datetime.now()
        super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.modifier = request.user
        obj.save()

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Log, LogAdmin)
