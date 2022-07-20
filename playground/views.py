import imp
from multiprocessing.sharedctypes import Value
from django.forms import DecimalField
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Customer, Product, OrderItem, Order
from django.db.models import Q,F,Value,Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max,Min,Avg

def say_hello(request):
    discounter_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
    queryset = Customer.objects.annotate(
        discounted_price  = discounter_price
    )


    return render(request,'hello.html',{'name':'Changhao'})