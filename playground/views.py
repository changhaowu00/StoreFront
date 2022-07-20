import imp
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product, OrderItem
from django.db.models import Q,F

def say_hello(request):
    qs= Product.objects.prefetch_related('collection').all()
    return render(request,'hello.html',{'name':'Changhao','products':list(qs)})