# from django.shortcuts import render
#
# def home(request):
#     return render(request, 'catalog/home.html')
#
# def contacts(request):
#     return render(request, 'catalog/contacts.html')

from django.shortcuts import render, get_object_or_404
from catalog.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def contacts(request):
    return render(request, 'catalog/contacts.html')
