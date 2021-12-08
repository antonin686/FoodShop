from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('category/<int:id>/products', views.categoryProducts, name='category_products'),
    path('products/<int:id>', views.productDetail, name='product_detail'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerUser, name='register'),
    path('logout', views.logoutUser, name='logout'),


    #api
    #path('', views.welcome)
]