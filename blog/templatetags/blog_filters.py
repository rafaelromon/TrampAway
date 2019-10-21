from django import template

register = template.Library()


@register.filter
def multiple(n, k):
    return not (n % k)
