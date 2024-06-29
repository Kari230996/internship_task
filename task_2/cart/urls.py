
from django.urls import path
from . import views

urlpatterns = [

    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('api/cart/', views.CartView.as_view(), name='cart_api'),
    path('api/cart/<int:pk>/', views.CartItemView.as_view(),
         name='cart_item_detail'),
    path('remove/<int:pk>/', views.remove_from_cart, name='cart_item_delete'),
    path('update/<int:pk>/', views.update_cart_item, name='update_cart_item'),

]
