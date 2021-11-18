from django.shortcuts import render
from django.http import HttpResponse
from .models import Collection, Product

def welcome(request):
    Collections = Collection.objects.all()
    context = {'collections' : Collections}
    return render(request, 'welcome.html', context)
