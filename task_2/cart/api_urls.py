from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartView.as_view(), name='cart_api'),
    path('<int:pk>/', views.CartItemView.as_view(), name='cart_item_detail'),
    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),

]
