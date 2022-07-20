import imp
from multiprocessing.sharedctypes import Value
from django.forms import DecimalField
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Customer, Product, OrderItem, Order
from django.db.models import Q,F,Value,Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max,Min,Avg

from django.contrib.contenttypes.models import ContentType
from store.models import Product
from django.db import models

from tags.models import TaggedItem


def say_hello(request):

    qs = TaggedItem.objects.get_tags_for(Product,1)

    return render(request,'hello.html',{'name':'Changhao','tags': list(qs)})