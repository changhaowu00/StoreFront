import imp
from multiprocessing.sharedctypes import Value
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Customer, Product, OrderItem, Order
from django.db.models import Q,F,Value,Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max,Min,Avg

def say_hello(request):

    queryset = Customer.objects.annotate(
        #CONCAT
        fullname = Func(
            F('first_name'),Value(' '),F('last_name'),function='CONCAT'
        )
    )

    queryset = Customer.objects.annotate(
        #CONCAT
        fullname = Concat(
            'first_name',Value(' '),'last_name'
        )
    )


    return render(request,'hello.html',{'name':'Changhao'})