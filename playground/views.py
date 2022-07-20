import imp
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from django.db.models import Q

def say_hello(request):
    #Products: inventory < 10 AND not price <20
    query_set = Product.objects.filter(Q(inventory__tl=10) & ~Q(unit_price__lt=20))
    return render(request,'hello.html',{'name':'Changhao','products':list(query_set)})