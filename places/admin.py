from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html

from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ("image", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px;" />', obj.image.url
            )
        return "Нет изображения"

    preview.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PlaceImageInline]
