from django.contrib import admin

# Register your models here.
from order.models import Order, User

admin.site.register(Order)

