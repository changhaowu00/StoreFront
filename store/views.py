from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from rest_framework import status

# Create your views here.

@api_view()
def product_list(request):
    queryset = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view()
def product_detail(request,id):

    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return  Response(status=status.HTTP_404_NOT_FOUND)

    product = get_object_or_404(product,pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)