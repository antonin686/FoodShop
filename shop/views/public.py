from django.shortcuts import redirect, render
from ..models import Category, Product

def welcome(request):
    categories = Category.objects.all()
    context = {'categories' :categories}
    return render(request, 'welcome.html', context)

