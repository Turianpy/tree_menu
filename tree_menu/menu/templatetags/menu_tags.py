from django import template
from ..models import MenuItem
from collections import defaultdict
from django.urls import reverse, NoReverseMatch


register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    I know this can be more compact if we use Prefetch,
    but that will always result in at least 2 queries afaik
    """
    items = MenuItem.objects.filter(menu__name=menu_name)

    children = defaultdict(list)
    for item in items:
        children[item.parent_id].append(item)

    root_items = children.pop(None, [])

    def build_tree(items):
        for item in items:
            item.desc = build_tree(children.pop(item.id, []))
        return items

    tree = build_tree(root_items)

    return {'items': tree, 'request': context['request']}


@register.simple_tag
def recur(menu_item):
    """
    helper func to recursively draw menu in the admin panel
    for better UX
    """
    return {'menu_item': menu_item, 'children': menu_item.children.all()}


@register.simple_tag
def get_url(item):
    """
    builds args list for reverse() from ancestor slugs and returns the result
    """
    try:
        args = []
        cur_item = item
        while cur_item.level > 0:
            args.insert(0, cur_item.slug)
            cur_item = cur_item.parent
        return reverse(item.named_url, args=args)
    except NoReverseMatch:
        print(f'No reverse match for {item.named_url} with args {args}')
        return item.url
