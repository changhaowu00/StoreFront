import imp
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product, OrderItem, Order
from django.db.models import Q,F
from django.db.models.aggregates import Count, Max,Min,Avg

def say_hello(request):
    result= Product.objects.aggregate(Count('id'),min_price = Min('unit_price'))
    return render(request,'hello.html',{'name':'Changhao','result':result})