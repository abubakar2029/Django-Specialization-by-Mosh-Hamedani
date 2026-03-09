from django.contrib import admin
from apps.storefront.models import OrderItem, Promotion, Collection, Product, Customer, Order
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
# from apps.tags.models import TaggedItem
# from django.contrib.contenttypes.admin import GenericTabularInline


admin.site.register(Promotion)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        url = (
            reverse("admin:storefront_product_changelist")
            + '?'
            + urlencode({'collection__id': str(collection.id)})
        )
        return format_html('<a href={}>{}</a>', url, collection.product_count)

    # over-riding base queryset
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(  # here we annotate the collection with the number of products in it
            # how many products are related to each collection
            product_count=Count('product')
        )


@admin.register(Customer)  # register decorator
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'email', 'membership']
    list_editable = ['membership']  # class attributes
    ordering = ['first_name', 'email']  # it makes no sense :)
    list_per_page = 10
    search_fields = ['first_name__istartswith']


class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low'),  # (value, display_name)
            ('>=10', 'OK')
        ]

    def queryset(self, request, queryset):
        # self.value(): Gets the selected value from the URL
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)
        if self.value() == '>=10':
            return queryset.filter(inventory__gte=10)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_id']
    list_per_page = 10
    list_select_related = ['collection']
    list_filter = ['collection', 'last_update', InventoryFilter]
    actions = ['clear_inventory']
    prepopulated_fields={
        'slug': ['title']
    }
    # inlines = [TagInline]
    search_fields = ['title__istartswith']

    def collection_id(self, product):
        return product.collection.id

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

    @admin.action(description='Clear inventory') 
    def clear_inventory(self, request, queryset):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request, f'{updated_count} products were successfully updated.')

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    autocomplete_fields = ['product']
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    inlines = [OrderItemInline]
    autocomplete_fields=['customer']