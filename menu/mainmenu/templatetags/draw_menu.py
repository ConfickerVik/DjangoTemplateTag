from django import template
from django.utils.safestring import mark_safe
from menu.mainmenu.models import MenuItems


register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):

    def render_menu(menu_items, class_ul="menu"):

        menu_html = f'<ul class="{class_ul}">'
        for item in menu_items:
            if item.link_url in menu_html:
                continue
            menu_html += '<li>'

            if item.menu_items.exists():
                if item.link_url.replace("/", "") in context["request"].get_full_path()[1:].replace("/", ""):
                    menu_html += f'<details open><summary><a href="{item.link_url}">{item.title}</a></summary>'
                else:
                    menu_html += f'<details><summary><a href="{item.link_url}">{item.title}</a></summary>'
                menu_html += render_menu(item.menu_items.all(), class_ul="submenu")
                menu_html += '</details>'
            else:
                menu_html += f'<a href="{item.link_url}">{item.title}</a>'

            menu_html += '</li>'
        menu_html += '</ul>'

        return menu_html

    query = MenuItems.objects.select_related("menu").filter(menu__name=menu_name)

    return mark_safe(render_menu(query))
