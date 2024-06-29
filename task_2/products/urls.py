

from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
    path('categories/<slug:category_slug>/',
         views.subcategory_list, name='subcategory_list'),
    path('subcategories/<slug:subcategory_slug>/',
         views.product_list, name='product_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
]
