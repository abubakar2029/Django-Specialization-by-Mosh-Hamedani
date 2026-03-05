from django.urls import path
from . import views
from . import orm_exercises
urlpatterns = [
    path('views/', views.dot_com_customers, name='views'), # the name attribute is to use in templates and views
    path('low_inventory/', views.low_inventory_products, name='low_inventory'), # the name attribute is to use in templates and views
    path('collection_3/', views.collection_3_order_items, name='collection_3_order_items'), # the name attribute is to use in templates and views
    path('defer_products/', views.defer_products, name='defer_products'), 
    path('ordered_items/', views.ordered_items, name='ordered_items'), # the name attribute is to use in templates and views
    path('hello/', views.hello_01, name='hello'),
    path('hello_02/', views.hello_02, name='hello_02'),
    path('hello_03/', views.hello_03, name='hello_03'),
    path('customer_1_orders/', orm_exercises.customer_1_orders, name='customer_1_orders'),
    path('product_1_sold_units/', orm_exercises.product_1_sold_units, name='product_1_sold_units'),
    path('annotate_example/', orm_exercises.annotate_example, name='annotate_example'),
]