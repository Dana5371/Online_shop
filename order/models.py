from datetime import datetime
from django.core.validators import RegexValidator

from django.db import models

from cart.models import ShoppingCart
from main.models import Product, User


class Order(models.Model):
    user = models.CharField(max_length=155, verbose_name='Пользователь')
    quantity_of_order = models.PositiveIntegerField(default=0, verbose_name='Кол-во заказов')
    total_price = models.PositiveIntegerField(default=0, verbose_name='Всего')
    price_with_discount = models.PositiveIntegerField(default=0,  verbose_name='Итог')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка')
    quantity_of_products = models.PositiveIntegerField(default=0, verbose_name='Кол-во продуктов')


    def save(self):
        self.user = str(User.objects.all())
        self.quantity_of_products = sum(i.products.amount * i.quantity for i in ShoppingCart.objects.all())
        self.total_price = sum(int(i.products.old_price) * int(i.quantity) for i in ShoppingCart.objects.all())
        self.price_with_discount = sum(int(i.products.new_price) * int(i.quantity) for i in ShoppingCart.objects.all())
        self.discount = self.total_price - self.price_with_discount
        self.quantity_of_order = ShoppingCart.objects.all().count()
        super(Order, self).save()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.quantity_of_products)


