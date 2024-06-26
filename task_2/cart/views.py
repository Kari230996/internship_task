from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Cart, CartItem
from .serializers import CartItemSerializer, CartSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def add_item(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        product = request.data.get('product')
        quantity = request.data.get('quantity', 1)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()
        return Response(CartSerializer(cart).data)

    @action(detail=False, methods=['post'])
    def remove_item(self, request):
        cart = Cart.objects.get(user=request.user)
        product = request.data.get('product')
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.delete()
        return Response(CartSerializer(cart).data)

    @action(detail=False, methods=['get'])
    def clear_cart(self, request):
        cart = Cart.objects.get(user=request.user)
        cart.items.clear()
        return Response(CartSerializer(cart).data)

    @action(detail=False, methods=['get'])
    def cart_detail(self, request):
        cart = Cart.objects.get(user=request.user)
        return Response(CartSerializer(cart).data)
