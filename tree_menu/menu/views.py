from django.shortcuts import render
from menu.models import MenuItem


def draw_menu(request, menu_name):
    menu_items = MenuItem.objects.filter(name=menu_name).select_related('parent')

    return render(request, 'menu/menu.html', {'menu_items': menu_items})

