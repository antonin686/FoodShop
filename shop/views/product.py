from pprint import pprint
from django.shortcuts import redirect, render
from ..models import Category, Product

def categoryProducts(request, id):
    category = Category.objects.get(pk=id) 
    products = category.product_set.all()
    #pprint(products)
    context = {
        'category' : category, 
        'products' : products
        }
    return render(request, 'category_products.html', context)

def productDetail(request, id):
    product = Product.objects.get(pk=id)
    context = { 'product': product }
    return render(request, 'product_detail.html', context)