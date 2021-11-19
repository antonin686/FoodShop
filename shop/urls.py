from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('category/<int:id>/products', views.category_products, name='category_products'),


    #api
    #path('', views.welcome)
]