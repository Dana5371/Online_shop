from datetime import datetime
from django.core.validators import RegexValidator

from django.db import models

from cart.models import ShoppingCart
from main.models import Product, User


# class Order(models.Model):
# user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
# quantity_of_order = models.PositiveIntegerField(default=0, verbose_name='Кол-во заказов')
# total_price = models.PositiveIntegerField(default=0, verbose_name='Всего')
# price_with_discount = models.PositiveIntegerField(default=0, verbose_name='Итог')
# discount = models.PositiveIntegerField(default=0, verbose_name='Скидка')
# quantity_of_products = models.PositiveIntegerField(default=0, verbose_name='Кол-во продуктов')
# product_list_in_cart = models.CharField(max_length=255, blank=True)
#
# def save(self):
#     self.quantity_of_products = sum(i.products.amount * i.quantity for i in ShoppingCart.objects.all())
#     self.total_price = sum(int(i.products.old_price) * int(i.quantity) for i in ShoppingCart.objects.all())
#     self.price_with_discount = sum(int(i.products.new_price) * int(i.quantity) for i in ShoppingCart.objects.all())
#     self.discount = self.total_price - self.price_with_discount
#     self.quantity_of_order = ShoppingCart.objects.all().count()
#     self.product_list_in_cart = str(i for i in ShoppingCart.objects.all())
#     print(print(i['ShoppingCart']) for i in ShoppingCart.objects.all())
#     super(Order, self).save()
#
# class Meta:
#     verbose_name = 'Заказ'
#     verbose_name_plural = verbose_name
#
# def __str__(self):
#     return str(self.quantity_of_products)


class Order(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)


    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="порядковый номер")
    total_price = models.PositiveIntegerField(default=0, verbose_name='Всего')
    price_with_discount = models.PositiveIntegerField(default=0, verbose_name='Итог')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка')
    products = models.CharField(max_length=255)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="добавить время")
    quantity_of_products = models.PositiveIntegerField(default=0, verbose_name='Кол-во продуктов')

    def save(self, *args, **kwargs):
        self.products = str(i.products for i in ShoppingCart.objects.all())
        self.quantity_of_products = sum(i.products.amount * i.quantity for i in ShoppingCart.objects.all())
        self.total_price = sum(int(i.products.old_price) * int(i.quantity) for i in ShoppingCart.objects.all())
        self.price_with_discount = sum(int(i.products.new_price) * int(i.quantity)
                                       for i in ShoppingCart.objects.all())

        self.discount = self.total_price - self.price_with_discount
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)
