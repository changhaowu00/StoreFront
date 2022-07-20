import imp
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from django.db.models import Q,F

def say_hello(request):
    product = Product.objects.all()[5:10]

    return render(request,'hello.html',{'name':'Changhao','products':product})