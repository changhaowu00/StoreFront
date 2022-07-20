import imp
from multiprocessing.sharedctypes import Value
from django.forms import DecimalField
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Customer, Product, OrderItem, Order
from django.db.models import Q,F,Value,Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max,Min,Avg

from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem

def say_hello(request):
    #getting tag of a product
    content_type = ContentType.objects.get_for_models(Product)
    qs = TaggedItem.objects\
        .select_related('tag')\
        .filter(
            content_type = content_type,
            object_id = 1
        )

    return render(request,'hello.html',{'name':'Changhao','tags': list(qs)})