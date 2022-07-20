import imp
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product
from django.db.models import Q,F

def say_hello(request):
    product = Product.objects.all().values('id','title','collection__title')#returns dictionaries
    product = Product.objects.all().values('id','title','collection__title')# returns list of tuples

    return render(request,'hello.html',{'name':'Changhao','products':product})