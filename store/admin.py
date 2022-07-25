from itertools import product
from urllib.parse import urlencode
from django.contrib import admin
from django.http import HttpRequest
from . import models
from django.db.models.aggregates import Count
from django.utils.html import format_html
from django.urls import reverse



#Or que can register using decorator istead of pasing the class as parameter
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','placed_at','customer']


@admin.register(models.Product) 
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','unit_price','inventory_status','collection_title']
    list_editable=['unit_price']
    list_per_page: int = 10

    list_select_related= ['collection']
    
    def collection_title(self,product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self,product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

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