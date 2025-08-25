# bakery/templatetags/cart_extras.py
from django import template
from bakery.models import Product   # <- Use your app name here, not relative import

register = template.Library()

@register.filter
def mul(value, arg):
    return value * arg

@register.filter
def product_by_id(product_id):
    try:
        return Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return None
