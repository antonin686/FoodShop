from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from ..models import Customer
from ..forms import RegisterForm

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