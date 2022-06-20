from django.db import models

# Create your models here.

from datetime import datetime
from django.core.validators import RegexValidator

from django.db import models
from cart.models import Cart


class Order(models.Model):
    """Информация о заказчике"""
    STATUS = [
        ('new', 'Новый'),
        ('issued', 'Оформлен'),
        ('cancelled', 'Отменен'),
    ]
    name = models.CharField(max_length=155, verbose_name='Имя')
    last_name = models.CharField(max_length=155, verbose_name='Фамилия')
    number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number_of_phone = models.CharField(validators=[number_regex], max_length=14, verbose_name='Номер телефона')
    country = models.CharField(max_length=200, verbose_name='Страна')
    city = models.CharField(max_length=155, verbose_name='Город')
    status_of_order = models.CharField(choices=STATUS, default='new', max_length=155, verbose_name='Статус заказа')

    """Order"""
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="порядковый номер")
    total_price = models.PositiveIntegerField(default=0, verbose_name='Всего')
    price_with_discount = models.PositiveIntegerField(default=0, verbose_name='Итог')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка')
    products = models.ManyToManyField(Cart)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="добавить время")
    quantity_of_products = models.PositiveIntegerField(default=0, verbose_name='Кол-во продуктов')

    def save(self, *args, **kwargs):
        """генерация порядкового номера"""
        from time import strftime
        from random import Random
        random_ins = Random()
        self.order_sn = "{time_str}{ranstr}".format(time_str=strftime("%Y%m%d%H%M%S"),
                                                    ranstr=random_ins.randint(10, 99))
        """Счет итога"""
        self.quantity_of_products = sum(i.quantity for i in Cart.objects.all())
        self.total_price = sum(int(i.color.products.old_price) * int(i.quantity) for i in Cart.objects.all())
        self.price_with_discount = sum(int(i.color.products.new_price) * int(i.quantity)
                                       for i in Cart.objects.all())
        self.discount = self.total_price - self.price_with_discount
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


