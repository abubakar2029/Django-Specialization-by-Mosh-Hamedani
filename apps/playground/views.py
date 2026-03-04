from django.shortcuts import render
from django.http import HttpResponse
from apps.storefront.models import Customer, Order, OrderItem, Product


# VIEWS Exercises
def collection_3_order_items(request):
    query_set = OrderItem.objects.filter(product__collection_id=3).values(
        'id', 'product__title', 'product__collection__title')

    return render(request, 'collection_3_order_items.html', {'products': query_set})



# Get last 5 Orders with their customers and items (incl products)
def last_5_orders_with_items(request):
    query_set = Order.objects.get_related('Customer').prefetch_related('orderitem_set__product').all()[:5]

    return render(request, 'last_5_orders_with_items.html', {'orders': query_set})


def ordered_items(request):
    query_set = OrderItem.objects.all().order_by('product__title').values(
        'product__id', 'product__title', 'product__unit_price').distinct()
    # using disctinct() because on product can appear in multiple order items
    return render(request, 'ordered_items.html', {'products': query_set})


def defer_products(request):
    query_set = Product.objects.only(
        'id', 'description', 'unit_price'
    ).order_by('id')

    return render(request, 'defer_products.html', {'products': query_set})


def low_inventory_products(request):
    query_set = Product.objects.filter(inventory__lte=10)

    return render(request, 'low_inventory_products.html', {'products': query_set})


def dot_com_customers(request):
    query_set = Customer.objects.filter(email__endswith='.com')

    return render(request, 'dot_com_customers.html', {'customers': query_set})


# HttpRequest raw content (string, HTML, JSON, etc.)
def hello_01(request):
    return HttpResponse("I am revising Django Concepts!")


def hello_02(request):
    return render(request, 'hello.html', {'name': 'Abubakar'})

# For Debugging Purpose


def hello_03(request):
    x = 2
    y = 3
    return HttpResponse(f"The sum of {x} and {y} is: {x+y}")
