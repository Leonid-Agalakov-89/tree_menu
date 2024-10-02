from django import template

from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    """Рендерит меню по имени."""
    # Получаем элементы меню с учетом родительских элементов
    menu_items = MenuItem.objects.filter(
        menu_name=menu_name, parent=None).prefetch_related('children')
    return menu_items
