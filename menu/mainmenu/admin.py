from django.contrib import admin
from .models import Menu, MenuItems


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "base_url"]


@admin.register(MenuItems)
class MenuItemsAdmin(admin.ModelAdmin):
    list_display = ["menu", "title", "description", "link_url", "parent"]

