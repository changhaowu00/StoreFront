from email.message import EmailMessage
import imp
from multiprocessing.sharedctypes import Value
from unicodedata import name
from django.forms import DecimalField
from django.http import HttpResponse
from django.shortcuts import render
from store.models import Collection, Customer, Product, OrderItem, Order
from django.db.models import Q,F,Value,Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max,Min,Avg

from django.contrib.contenttypes.models import ContentType
from store.models import Product
from django.db import models

from tags.models import TaggedItem

from django.db import transaction

from django.db import connection
from django.core.mail import send_mail, mail_admins, BadHeaderError

from templated_mail.mail import BaseEmailMessage

def say_hello(request):
    """
    qs = Product.objects.raw('SELECT * FROM store_product')

    #or
    cursor = connection.cursor()
    cursor.execute('sql')
    cursor.close()

    #better
    with connection.cursor() as cursor:
        cursor.execute('sql')

    #better
    with connection.cursor() as cursor:
        cursor.callproc('name procedure',[1,2,3])

    return render(request,'hello.html',{'name':'Changhao','tags': list()})
    """
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name':'CHAng'}
        )
        message.send(['john@moshbuy.com'])
    except BadHeaderError:
        pass
    return render(request,'hello.html',{'name':'Mosh'})