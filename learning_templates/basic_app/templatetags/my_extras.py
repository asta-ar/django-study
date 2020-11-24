from django import template

register = template.Library()

@register.filter(name='cut')  #USING PYTHON DECORATORS
def cut(value,arg):
    """
    This cuts out all values of arg from string!
    """
    return value.replace(arg,'')

#register.filter('cut',cut) #first cut is a string that you pass to the function, second is a function
