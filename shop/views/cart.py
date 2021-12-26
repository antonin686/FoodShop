
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import F, DecimalField, ExpressionWrapper, Sum
from django.contrib import messages

from pprint import pprint
from ..models import Cart, CartItem, Customer, Order, OrderItem
from ..forms import CheckoutForm


def checkout(request):
    user = request.user

    if not hasattr(user, 'customer'):
        Customer.objects.create(user=user)

    if request.user.is_authenticated:
        customer_id = request.user.customer.id
        cart = Cart.objects.filter(customer_id=customer_id).first()
        user = request.user
        if cart is not None and hasattr(cart, 'items'):

            if request.method == 'POST':
                form = CheckoutForm(request.POST)
                if form.is_valid():
                    form.instance.customer_id = user.customer.id
                    order = form.save()
                    #pprint(order.id)
                    for item in cart.items.all():
                        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
                    cart.delete()
                    messages.success(request, 'Order has been placed')
                    return redirect('confirm_msg')
            else:
                initial = {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'phone': user.customer.phone,
                    'address': user.customer.address,
                    'city': user.customer.city}
                form = CheckoutForm(initial=initial)
                items = cart.items.annotate(total=ExpressionWrapper(
                    F('product__price') * F('quantity'), output_field=DecimalField(decimal_places=2)))
                items = list(items.values('id', 'cart_id', 'product__name',
                             'quantity', 'total', 'product__image', 'product__price'))
                count = list(cart.items.all().aggregate(
                    res=Sum(F('quantity') * F('product__price'))).values())
                context = {'items': items,
                           'total': count[0], 'currency': 'BDT', 'form': form}

                return render(request, 'checkout.html', context)

    return render(request, 'checkout.html')
