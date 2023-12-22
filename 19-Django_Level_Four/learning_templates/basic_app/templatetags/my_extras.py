# custom template tag filters defined here!

from django import template 

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """ This cuts out all instances of "arg" from the string """

    return value.replace(arg, '')


# register.filter('cut', cut) # other way to register,  but decorator approach above is best