from django import template

register = template.Library()


@register.filter(name='endswith')
def endswith(value, arg):
    if isinstance(value, str):
        return value.endswith(arg)
    return False
