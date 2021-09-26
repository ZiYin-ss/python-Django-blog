# coding=utf-8

from django.template import Library

register = Library()


@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)

@register.filter
def cd(value):
    a=value.split('-')
    c=a[0]+'年'+a[1]+'月'
    return c

@register.filter
def ad(value):
    a=value.split('-')
    b=a[0]
    return b

@register.filter
def bd(value):
    a=value.split('-')
    d=a[1]
    return d
