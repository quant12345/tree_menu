from django.contrib import admin
from menu.models import MenuItem

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'named_url', 'parent')
    list_filter = ('name',)
    search_fields = ('name', 'named_url')
    ordering = ('id',)

admin.site.register(MenuItem, MenuItemAdmin)
