from django.db import transaction
from django.shortcuts import render
from apps.storefront.models import CartItem, Cart, Customer, Order, OrderItem, Product
from django.db.models.aggregates import Count
from django.db.models import Value
from django.db.models.functions import Concat

# How many orders has customer 1 placed?


def customer_1_orders(request):
    o_count = Customer.objects.filter(id=1).aggregate(Count('order'))

    return render(request, 'customer_1_orders.html', {'total': o_count['orders__count']})


# How many units of product 1 have we sold?
def product_1_sold_units(request):
    total = OrderItem.objects.filter(product_id=1).aggregate(Count('quantity'))

    return render(request, 'product_1_sold_units.html', {'total': total['quantity__count']})


def annotate_example(request):
    query_set = Product.objects.annotate(new_Field=Value(True))

    return render(request, 'hello.html', {'products': list(query_set)})

# database func.


def concat_name(request):
    query_set = Customer.objects.annotate(
        full_name=Concat("first_name", Value(' '), "last_name")
    )

    return render(request, 'hello.html', {'customers': list(query_set)})

# • Create a shopping cart with an item
# • Update the quantity of an item in a shopping cart
# • Remove a shopping cart with its items

def create_cart(request):
    cart = Cart.objects.create()
    product = Product.objects.get(id=1)
    CartItem.objects.create(cart=cart, product=product, quantity=2)


    return render(request, 'hello.html', {'cart': cart})

@transaction.atomic()
def update_cart(request):
    cart_item = CartItem.objects.get(id=1)
    cart_item.quantity = -5
    cart_item.save()

    return render(request, 'hello.html', {'cart_item': cart_item})