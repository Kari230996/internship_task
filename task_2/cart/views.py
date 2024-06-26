from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product
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


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')


@login_required
def remove_from_card(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart_detail')


@login_required
def clear_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart.items.clear()
    return redirect('cart_detail')
