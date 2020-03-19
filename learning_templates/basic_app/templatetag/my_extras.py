from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value,arg):
    """
    THIS CUTS OUT ALL VALUE OF ARG FROM STRING
    """
    return value.replpace(arg,'')


# register.filter('cut',cut)
