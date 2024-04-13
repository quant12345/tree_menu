from django.shortcuts import render


def draw_menu(request, menu_name):

    return render(request, 'menu/menu.html', context={'url': menu_name})

