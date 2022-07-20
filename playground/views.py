from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def say_hello(request):
    query_set = Product.objects.filter(title__startswith='cofee')#endfswith
    return render(request,'hello.html',{'name':'Changhao','products':list(query_set)})