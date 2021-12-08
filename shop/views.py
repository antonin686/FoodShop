from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .models import Category, Product, Customer
from .forms import RegisterForm

from pprint import pprint

def welcome(request):
    categories = Category.objects.all()
    context = {'categories' :categories}
    return render(request, 'welcome.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else: 
            context = {
                'error': 'Given Credentials Does not match'
            }
            return render(request, 'accounts/login.html', context)
   
    return render(request, 'accounts/login.html')

def registerUser(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        pprint("POST")
        if form.is_valid():
            user = form.save()
            phone = form.cleaned_data.get('phone')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(user=user, phone=phone)
            return redirect('login')

    #pprint("dsa")
    context = {'form': form}

    return render(request, 'accounts/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def categoryProducts(request,id):
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
