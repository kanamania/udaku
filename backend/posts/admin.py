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
    list_display = ["show_name", "category", "creator", 'created_at', 'status']
    search_fields = ('name', 'category')
    ordering = ('name', 'category')
    filter_horizontal = ()

    def show_name(self, obj):
        url = reverse('admin:%s_%s_detail' % (obj._meta.app_label, obj._meta.model_name), args=[obj.id])
        return format_html("<a href='{url}'>{name}</a>", url=url, name=obj.name)

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
