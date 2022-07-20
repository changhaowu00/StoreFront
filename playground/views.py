import imp
from multiprocessing.sharedctypes import Value
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Customer, Product, OrderItem, Order
from django.db.models import Q,F,Value
from django.db.models.aggregates import Count, Max,Min,Avg

def say_hello(request):
    Customer.objects.annotate(new_id = Value(True))
    Customer.objects.annotate(new_id = F('id')+1)
    return render(request,'hello.html',{'name':'Changhao','result':result})