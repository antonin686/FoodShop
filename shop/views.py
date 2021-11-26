from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product
from pprint import pprint

def welcome(request):
    categories = Category.objects.all()
    context = {'categories' :categories}
    return render(request, 'welcome.html', context)

def category_products(request,id):
    category = Category.objects.get(pk=id) 
    products = category.product_set.all()
    #pprint(products)
    context = {
        'category' : category, 
        'products' : products
        }
    return render(request, 'category_products.html', context)

def product_detail(request, id):
    product = Product.objects.get(pk=id)
    context = { 'product': product }
    return render(request, 'product_detail.html', context)
