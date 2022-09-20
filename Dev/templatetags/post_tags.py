from pickle import TRUE
from django import template
from ..models import*
register = template.Library()


@register.filter(name="is_exit_in_cart")
def is_exit_in_cart(product,cart):
    key=cart.keys()
    for id in key:
        if int(id)==product.id:
            return True
    return False
@register.filter(name="cartquntity")
def cartquntity(product,cart):
    key=cart.keys()
    for id in key:
        if int(id)==product.id:
            return cart.get(id)
    return False

@register.filter(name="Total_price")
def Total_price(product,cart):
    c=product.price*cartquntity(product,cart)
    return c

@register.filter(name="Payable_price")
def Payable_price(product,cart):
    s=0
    for i in product:
        s=s+Total_price (i,cart)
    return s

@register.filter(name="order_amount")
def order_amount(num1,num2):
    return num1*num2
    