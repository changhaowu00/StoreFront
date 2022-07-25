from itertools import product
from operator import invert
from urllib.parse import urlencode
from django.contrib import admin
from django.http import HttpRequest

from tags.models import TaggedItem
from . import models
from django.db.models.aggregates import Count
from django.utils.html import format_html
from django.urls import reverse

from django.contrib.contenttypes.admin import GenericTabularInline

#Or que can register using decorator istead of pasing the class as parameter
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','customer']

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10','Low')
        ]

    def queryset(self, request, queryset) :
        if self.value()=='<10':
            return queryset.filter(inventory__lt=10)


class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


@admin.register(models.Product) 
class ProductAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    autocomplete_fields=['collection']
    prepopulated_fields={
        'slug':['title']
    }


    actions ='clear_inventory'
    list_display = ['title','unit_price','inventory_status','collection_title']
    list_editable=['unit_price']
    list_per_page: int = 10

    list_select_related= ['collection']
    list_filter = ['collection','last_update']

    def collection_title(self,product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

    @admin.action(description='Clear inventory')
    def clear_inventory(self,request,queryset):
        updated_count = queryset.update(inventory = 0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated'

        )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','membership']
    list_editable = ['membership']
    ordering = ['first_name','last_name']
    list_per_page = 10
    search_fields = ['first_name__istartswith','last_name__istartwith']

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title','products_count']
    search_fields = ['title']

    @admin.display(ordering= 'products_count')
    def products_count(self,collection):
        url = (
            reverse('admin:store_product_changelist') 
            + '?'
            + urlencode({
                'collection_id':str(collection.id)
            })
            )
        return format_html('<a href="{}">{}</a>',url,collection.products_count)

    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).annotate(
            products_count = Count('product')
        )

#admin.site.register(models.Product,ProductAdmin)