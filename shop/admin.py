from django.contrib import admin
from . import models

admin.site.register(models.Collection)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 10
