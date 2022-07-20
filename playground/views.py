from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product

def say_hello(request):
    query_set = Product.objects.filter(collection__id__range=(1,2,3))
    return render(request,'hello.html',{'name':'Changhao','products':list(query_set)})