from django import template
from menu.models import MenuItem
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(name=menu_name).select_related('parent')

    return mark_safe(generate_menu(menu_items))


def generate_menu(menu_items):
    generate_html = '<ul>'
    for item in menu_items:
        generate_html += '<li>'
        if item.named_url:
            generate_html += f'<a href="{item.named_url}">{item.name}</a>'
        else:
            generate_html += item.name
        if item.children.exists():
            generate_html += generate_menu(item.children.all())
        generate_html += '</li>'
    generate_html += '</ul>'

    return generate_html