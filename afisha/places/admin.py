from django.contrib import admin
from django.utils import html

from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase

from places.models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    fields = ('url', 'get_preview', 'order_number')
    readonly_fields = ['get_preview']
    extra = 1

    def get_preview(self, obj):
        return html.format_html(
            '<img src="{}" height="{}"/>',
            obj.absolute_image_url,
            obj.url.height if obj.url.height < 200 else 200
        )


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return html.format_html(
            '<img src="{}" height="{}"/>',
            obj.absolute_image_url,
            obj.url.height if obj.url.height < 200 else 200
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline
    ]
