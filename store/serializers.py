
import collections
from turtle import title
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection

class CollectionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)

class ProductSerializer(serializers.Serializer):
    id =serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6,decimal_places=2,source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # collection = serializers.PrimaryKeyRelatedField(
    #     queryset=Collection.objects.all()
    # )
    # collection = serializers.StringRelatedField(
    #     queryset=Collection.objects.all()
    # )

    collection = CollectionSerializer()


    def calculate_tax(self,product):
        return product.unit_price * Decimal(1.1)