from django.contrib import admin
from apps.storefront.admin import ProductAdmin
from apps.storefront.models import Product
from apps.tags.models import TaggedItem
from django.contrib.contenttypes.admin import GenericTabularInline

class TagInline(GenericTabularInline):
    model = TaggedItem
    extra = 1

class CustomProductAdmin(ProductAdmin): # it extends the default ProductAdmin
    inlines = [TagInline]

admin.site.unregister(Product) 
admin.site.register(Product, CustomProductAdmin)