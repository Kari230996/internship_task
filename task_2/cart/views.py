from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Product
from .models import CartItem, Cart
from .serializers import CartItemSerializer, CartSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.utils.decorators import method_decorator

from django.http import HttpResponseRedirect
from django.urls import reverse


class CartView(APIView):
    def get(self, request):
        cart, created = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        cart_item.save()

        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CartItemView(APIView):
    def delete(self, request, pk):
        try:
            cart_item = get_object_or_404(
                CartItem, pk=pk, cart__user=request.user)
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    print(f'Cart items for {request.user.username}: {cart.items.all()}')
    referer = request.session.get('referer')
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'referer': referer})


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    print(
        f'Added {product.name} to cart for {request.user.username}. Cart created: {created}')

    referer = request.META.get('HTTP_REFERER')
    request.session['referer'] = referer

    return redirect('cart_detail')


@login_required
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
    cart_item.delete()
    return redirect('cart_detail')


@login_required
def update_cart_item(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart_detail')
