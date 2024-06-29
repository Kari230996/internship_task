from rest_framework import serializers
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):

    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.FloatField(
        source='product.price', read_only=True)
    total_price = serializers.FloatField(source='total_price', read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name',
                  'product_price', 'quantity', 'total_price']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.FloatField(source='total_price', read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price']
