from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.db.models import Sum
from ..models import Cart, CartItem, Customer
from pprint import pprint


def getCartInfo(request):
    if request.user.is_authenticated and hasattr(request.user, 'customer'):
        customer_id = request.user.customer.id
        cart = Cart.objects.filter(customer_id=customer_id).first()
        if cart is not None and hasattr(cart, 'items'):
            items = list(cart.items.all().values(
                'id', 'cart_id', 'product__name', 'quantity', 'product__image', 'product__price'))
            count = list(cart.items.all().aggregate(Sum('quantity')).values())
            res = {
                'count': count[0],
                'items': items
            }
            return JsonResponse(res, safe=False)

    return JsonResponse([], safe=False)


def addToCart(request):
    user = request.user
    if user.is_authenticated:
        if not hasattr(user, 'customer'):
            Customer.objects.create(user=user)
        customer_id = user.customer.id
        cart = Cart.objects.filter(customer_id=customer_id).first()
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        if int(quantity) > 0:
            if cart is None:
                cart = Cart.objects.create(customer_id=customer_id)
            CartItem.objects.create(
                cart_id=cart.id, product_id=product_id, quantity=quantity)
            return HttpResponse("success")

    return HttpResponse("fail")


def updateCart(request):
    if request.user.is_authenticated:
        cartitem_id = request.POST.get('cartitem_id')
        quantity = request.POST.get('quantity')
        if int(quantity) > 0:
            cartitem = CartItem.objects.get(pk=cartitem_id)
            cartitem.quantity = quantity
            cartitem.save()
            return HttpResponse("success")

    return HttpResponse("failed")


def deleteCart(request):
    if request.user.is_authenticated:
        cartitem_id = request.POST.get('cartitem_id')

        cartitem = CartItem.objects.get(pk=cartitem_id)
        cartitem.delete()

        return HttpResponse("success")

    return HttpResponse("fail")
