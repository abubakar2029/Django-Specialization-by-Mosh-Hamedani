from django.shortcuts import render
from apps.storefront.models import Customer, Order, OrderItem, Product
from django.db.models.aggregates import Count


# How many orders has customer 1 placed?
def customer_1_orders(request):
    o_count = Customer.objects.filter(id=1).aggregate(Count('order'))

    return render(request, 'customer_1_orders.html', {'total': o_count['orders__count']})


# How many units of product 1 have we sold?
def product_1_sold_units(request):
    total = OrderItem.objects.filter(product_id=1).aggregate(Count('quantity'))

    return render(request, 'product_1_sold_units.html',{'total': total['quantity__count']})


