from django.shortcuts import render
from .models import Category, Product


# Create your views here.

def index(request):
    """For home page"""

    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/index.html', context=context)


def all_product_by_category(request, category_slug):
    """For sort by category"""

    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category=category)

    return render(request, 'shop/index.html', context={'products': products, 'categories': categories})


def product_detail(request, pk):
    """For product details"""

    categories = Category.objects.all()
    product = Product.objects.get(pk=pk)

    return render(request, 'shop/product_detail.html', context={'product': product, 'categories': categories})
