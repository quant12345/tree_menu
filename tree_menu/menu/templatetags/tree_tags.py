from django import template
from menu.models import MenuItem
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    data = MenuItem.objects.values('name', 'named_url', 'parent__name')

    return mark_safe(generate_main(menu_name, data))


def generate_inside_main(name, data):
    generate_html = '<ul>'
    for entry in data:
        if name == entry['parent__name']:
            generate_html += '<li>'
            generate_html += f'<a href="{entry["named_url"]}">{entry["name"]}</a>'
            resalt_recursion = generate_inside_main(entry['name'], data)
            ul_end = '</ul>'
            if len(resalt_recursion) <= 4:
                ul_end = ''
                resalt_recursion = ''
            generate_html += resalt_recursion
            generate_html += '</li>' + ul_end
    return generate_html


def generate_main(name, data):
    inside_main = generate_inside_main(name, data)
    first_url = [i['named_url'] for i in data if name == i['name']]
    link = f'<a href="{first_url[0]}">{name}</a>'
    generate_html = '<ul><li>'
    generate_html += link
    generate_html += inside_main
    generate_html += '</li></ul>'
    return generate_html
