from django import template

register = template.Library()


@register.filter(name='includes')
def includes(value, args):
    if args in value:
        return 'w3-yellow'
    else:
        return ''
