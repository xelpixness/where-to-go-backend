from django.contrib import admin
from .models import Place, PlaceImage
from django.utils.html import format_html


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ("image", "preview", "position")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height: 100px;" />', obj.image.url
            )
        return "Нет изображения"

    preview.short_description = "Превью"


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]
