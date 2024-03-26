from django.urls import path, include
from menu.views import draw_menu


app_name = 'menu'

urlpatterns = [
    path('<str:menu_name>/', draw_menu, name='draw_menu'),
]

