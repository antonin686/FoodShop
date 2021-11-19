from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ['name']
    }
    autocomplete_fields = ['category']
    list_per_page = 10

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['name']
