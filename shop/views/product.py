from pprint import pprint
from django.shortcuts import redirect, render
from ..models import Category, Product


def categoryProducts(request, id):
    category = Category.objects.get(pk=id)
    products = category.product_set.all()
    # pprint(products)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category_products.html', context)


def productShow(request, id):
    product = Product.objects.get(pk=id)
    extraimages = product.images.all()
    similarproducts = Product.objects.filter(category_id = product.category_id)
    context = {
        'product': product,
        'extraimages': extraimages,
        'similarproducts': similarproducts,
        'currency': 'BDT'
    }
    return render(request, 'products/show.html', context)
