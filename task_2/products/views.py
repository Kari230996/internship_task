# products/views.py

from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Category, SubCategory, Product
from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer
from django.core.paginator import Paginator


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [permissions.AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


def home(request):
    return render(request, 'home.html')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def subcategory_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategories = category.subcategories.all()
    return render(request, 'subcategory_list.html', {'category': category, 'subcategories': subcategories})


def product_list(request, subcategory_slug):
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
    products = subcategory.products.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'products/product_list.html', {'subcategory': subcategory, 'page_obj': page_obj, 'category': subcategory.parent_category})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'products/product_detail.html', {'product': product})
