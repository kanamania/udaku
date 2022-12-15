from datetime import datetime

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.urls import reverse
from django.utils.html import format_html

from .forms import *
from .models import *


class PostAdmin(ModelAdmin):
    add_form = PostCreationForm
    form = PostChangeForm
    model = Post
    list_display = ["show_name", "category", "description", "creator", 'created_at', 'status', 'show_actions']
    search_fields = ('name', 'category', 'description', 'body')
    ordering = ('name', 'category')
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


class PostCategoryAdmin(ModelAdmin):
    add_form = PostCategoryCreationForm
    form = PostCategoryChangeForm
    model = PostCategory
    list_display = ["show_name", "category", "creator", 'created_at', 'status', 'show_actions']
    search_fields = ('name', 'category')
    ordering = ('name', 'category')
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


class PostCommentAdmin(ModelAdmin):
    add_form = PostCommentCreationForm
    form = PostCommentChangeForm
    model = PostComment
    list_display = ["show_name", "description", "creator", 'created_at', 'status', 'show_actions']
    search_fields = ('post', 'description')
    ordering = ('post', 'created_at')
    filter_horizontal = ()

    def show_name(self, obj):
        url = reverse('%s_%s_detail' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html("<a href='{url}'>{name}</a>", url=url, name=obj.post)
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


admin.site.register(Post, PostAdmin)
admin.site.register(PostComment, PostCommentAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
