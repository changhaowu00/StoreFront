from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def say_hello(request):
    query_set = Product.objects.filter(unit_price__range = (20,30))
    return render(request,'hello.html',{'name':'Changhao','products':list(query_set)})