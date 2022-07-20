import imp
from multiprocessing.sharedctypes import Value
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Customer, Product, OrderItem, Order
from django.db.models import Q,F,Value,Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max,Min,Avg

def say_hello(request):

    queryset = Customer.objects.annotate(
        orders_count = Count('order')
    )


    return render(request,'hello.html',{'name':'Changhao'})