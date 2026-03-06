from django.contrib import admin
from apps.storefront.models import Promotion, Collection, Product, Customer, Order
from django.db.models.aggregates import Count


admin.site.register(Promotion)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        return collection.product_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count('product')
        )


@admin.register(Customer)  # register decorator
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'membership']
    list_editable = ['membership']  # class attributes
    ordering = ['first_name', 'email']  # it makes no sense :)
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_id']
    list_per_page = 10
    list_select_related = ['collection']

    def collection_id(self, product):
        return product.collection.id

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
