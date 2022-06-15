from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('products', 'quantity')
