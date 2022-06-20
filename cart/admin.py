from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(Cart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('color', 'quantity')
