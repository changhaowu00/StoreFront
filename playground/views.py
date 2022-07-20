import imp
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from django.db.models import Q,F

def say_hello(request):
    query_set = Product.objects.filter(inventory = F('unit_price'))
    return render(request,'hello.html',{'name':'Changhao','products':list(query_set)})