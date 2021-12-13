from django.urls import path

from shop.views.api import addToCart
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('category/<int:id>/products', views.categoryProducts, name='category_products'),
    path('products/<int:id>', views.productDetail, name='product_detail'),
    path('login', views.loginPage, name='login'),
    path('register', views.registerUser, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('checkout', views.checkout, name='checkout'),


    #api
    path('api/getCartDetails', views.getCartInfo, name="api_getCartDetails"),
    path('api/addToCart', views.addToCart, name="api_addToCart"),
    path('api/updateCart', views.updateCart, name="api_updateCart"),
    path('api/deleteCart', views.deleteCart, name="api_deleteCart"),
]