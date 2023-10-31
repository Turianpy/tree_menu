from django import template
from ..models import MenuItem
from collections import defaultdict


register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_name):
    items = MenuItem.objects.filter(menu__name=menu_name).order_by('order')

    children = defaultdict(list)
    for item in items:
        children[item.parent_id].append(item)

    root_items = children.pop(None, [])

    def build_tree(items):
        for item in items:
            item.desc = build_tree(children.pop(item.id, []))
        return items

    tree = build_tree(root_items)

    return {'items': tree}


@register.simple_tag
def recur(menu_item):
    return {'menu_item': menu_item, 'children': menu_item.children.all()}