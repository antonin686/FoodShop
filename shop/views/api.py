from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.db.models import Sum
from ..models import Cart, CartItem
from pprint import pprint

def getCartInfo(request):
    user_id = request.user.id
    
    if user_id is not None:
        cart = Cart.objects.filter(user_id=user_id).first()
        if cart is not None and hasattr(cart, 'items'):
            items = list(cart.items.all().values('id', 'cart_id', 'product__name', 'quantity', 'product__image', 'product__price'))
            count = list(cart.items.all().aggregate(Sum('quantity')).values())
            res = {
                'count': count[0],
                'items': items
            }
            return JsonResponse(res, safe=False)
    
    return JsonResponse([], safe=False)

def addToCart(request):
    user_id = request.user.id
    cart = Cart.objects.filter(user_id=user_id).first()
    product_id = request.POST.get('product_id')
    quantity = request.POST.get('quantity')

    if cart is None:
        cart = Cart.objects.create(user_id=user_id)
        
    CartItem.objects.create(cart_id=cart.id, product_id=product_id, quantity=quantity)

    return HttpResponse("success")


def updateCart(request):
    cartitem_id = request.POST.get('cartitem_id')
    quantity = request.POST.get('quantity')

    cartitem = CartItem.objects.get(pk=cartitem_id)
    cartitem.quantity = quantity
    cartitem.save(update_fields = ['quantity'])

    return HttpResponse("success")

def deleteCart(request):
    cartitem_id = request.POST.get('cartitem_id')

    cartitem = CartItem.objects.get(pk=cartitem_id)
    cartitem.delete() 

    return HttpResponse("success")