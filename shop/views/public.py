from django.shortcuts import redirect, render
from ..models import Category, Product, OrderItem
from django.db.models import Sum, F, Count
from pprint import pprint
from datetime import timedelta
from django.utils import timezone


def welcome(request):

    thirty_days_ago = timezone.now() - timedelta(days=30)
    categories = Category.objects.all()
    popular = OrderItem.objects.filter(created_at__gte=thirty_days_ago).values(
        'product_id', 'product__name', 'product__image', 'product__price').annotate(total=Sum('quantity')).order_by('total')
    context = {'categories': categories, 'popular': popular}
    #pprint(popular)

    return render(request, 'welcome.html', context)


def confirmMsg(request):

    return render(request, 'confirm_msg.html')
