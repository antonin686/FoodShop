from pprint import pprint
from django.shortcuts import redirect, render
from ..models import Category, Product, Review
from .helper import checkIfCanReview
from django.db.models.functions import Concat
from django.db.models import Value

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
    similarproducts = Product.objects.filter(category_id = product.category_id).exclude(id=product.id)
    #pprint(similarproducts)
    reviews = Review.objects.filter(product_id=product.id)
    canReview = checkIfCanReview(request.user.customer.id, product.id)
    
    context = {
        'product': product,
        'extraimages': extraimages,
        'similarproducts': similarproducts,
        'reviews': reviews,
        'canReview': canReview,
        'currency': 'BDT',
        'profileimg': 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
    }
    return render(request, 'products/show.html', context)
