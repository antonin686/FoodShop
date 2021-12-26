from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.http import request
from .models import Order

class RegisterForm(UserCreationForm): 
    password1 = forms.CharField(label='Password', max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone', max_length=16, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'phone', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  
        }
        help_texts = {
            'username': None,
        }

class CheckoutForm(ModelForm):
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone', 'email', 'city', 'comment']
        exclude = ['customer_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),  
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  
            'phone': forms.TextInput(attrs={'class': 'form-control'}),    
            'address': forms.TextInput(attrs={'class': 'form-control'}),  
            'city': forms.TextInput(attrs={'class': 'form-control'}),  
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 2, "blank":True}),  
        }