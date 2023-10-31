from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import MenuItem, Menu


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 0
    fk_name = 'parent'


class MenuItemInlineForMenu(admin.TabularInline):
    model = MenuItem
    extra = 0
    fk_name = 'menu'
    readonly_fields = ('view_link', )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(parent__isnull=True)

    def view_link(self, obj):
        url = reverse('admin:menu_menuitem_change', args=(obj.id,))
        return format_html('<a href="{}?parent={}">View</a>', url, obj.id)
    view_link.short_description = 'View'


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'url')
    list_filter = ('menu',)
    search_fields = ('name', 'url')
    inlines = (MenuItemInline,)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'named_url')
    search_fields = ('name',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        menu = Menu.objects.get(pk=object_id)
        items = MenuItem.objects.filter(menu=menu, parent__isnull=True)
        extra_context['items'] = items
        return super().change_view(
            request, object_id, form_url, extra_context=extra_context,
        )

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)
