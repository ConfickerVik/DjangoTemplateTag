from django import template
from django.utils.safestring import mark_safe
from menu.mainmenu.models import MenuItems


register = template.Library()


@register.simple_tag
def draw_menu(menu_name):

    def render_menu(menu_items):

        menu_html = '<ul>'
        for item in menu_items:
            if item.link_url in menu_html:
                continue
            menu_html += '<li>'
            if item.link_url:
                menu_html += f'<a href="{item.link_url}">{item.title}</a>'
            else:
                menu_html += item.title
            if item.menu_items.exists():
                menu_html += render_menu(item.menu_items.all())
            menu_html += '</li>'
        menu_html += '</ul>'

        return menu_html

    query = MenuItems.objects.select_related("menu").filter(menu__name=menu_name)#.values().order_by("parent_id").values_list(
    #    "menu__name",
    #    "menu__base_url",
    #    "id",
    #    "title",
    #    "link_url",
    #    "parent_id"
    #)

    return mark_safe(render_menu(query))
