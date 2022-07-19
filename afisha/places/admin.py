from django.contrib import admin
from django.utils import html

from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase

from places.models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    fields = ('file', 'get_preview', 'order_number')
    readonly_fields = ['get_preview']
    extra = 1

    def get_preview(self, obj):
        return html.format_html(
            '<img src="{}" style="max-height: 200px">',
            obj.absolute_image_url
        )


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    readonly_fields = ['get_preview']

    def get_model_perms(self, request):
        if not request.user.has_perm('can_see_image_model'):
            return {}
        return super().get_model_perms(request)

    def get_preview(self, obj):
        return html.format_html(
            '<img src="{}" style="max-height: 200px">',
            obj.absolute_image_url
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    search_fields = [
        'title'
    ]
    inlines = [
        ImageInline
    ]
