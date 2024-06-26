from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet
from . import views

router = DefaultRouter()
router.register(r'cart', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>/', views.remove_from_card, name='remove_from_cart'),
    path('clear/', views.clear_cart, name='clear_cart'),

]
