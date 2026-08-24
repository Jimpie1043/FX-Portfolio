# documentation/admin.py
from django.contrib import admin

from .models import Document, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    list_filter = ("tags",)
    search_fields = ("title", "description")
    filter_horizontal = ("tags",)
    readonly_fields = ("preview_image", "created_at", "updated_at")
    fields = ("title", "description", "pdf", "preview_image", "tags", "created_at", "updated_at")