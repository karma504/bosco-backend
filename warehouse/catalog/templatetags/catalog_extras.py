from django import template
from ..models import Product

register = template.Library()


@register.filter
def uah(value):
    return f"{value} грн"


@register.filter
def weight(grams):
    if grams >= 1000:
        return f"{grams / 1000:g} кг"
    return f"{grams} г"


@register.simple_tag
def product_count():
    return Product.objects.count()