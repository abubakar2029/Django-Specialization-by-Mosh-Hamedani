from django.contrib import admin
from django.urls import reverse
from apps.storefront.models import OrderItem
from .models import Product, Collection, Order
from django.db.models import Count
from django.utils.html import format_html, urlencode


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory', 'stock']
    list_per_page = 20
    ordering = ['unit_price']
    actions = ['clear_inventory']
    search_fields = ['title']
    prepopulated_fields = {
        'slug': ['title']
    }

    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{updated_count} products removed from inventory'
        )

    def stock(self, product):
        if product.inventory > 0:
            return "In Stock"
        return "Out of Stock"

    def lookups(self, request, model_admin):
        return [
            ('<5', 'Low Stock'),
            ('>=5', 'Sufficient Stock')
        ]

    def queryset(self, request, queryset):
        if self.value() == "<5":
            return queryset.filter(product_inventory__lt=5)
        return queryset.filter(product_inventory__gte=5)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    def product_count(self, collection):
        url = (reverse('admin:storefront_product_changelist')
               + '?'
               + urlencode({
                   'collection_id': str(collection.id)
               }))

        return format_html('<a href={}>{}</a>', url, collection.product_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count=Count('product')
        )

class OrderItemInline(admin.TabularInline):
    model=OrderItem
    extra=2
    autocomplete_fields=['product']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    inlines=[OrderItemInline]

