from django.contrib import admin

# Register your models here.
from account.models import User

@admin.register(User)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('email',)
