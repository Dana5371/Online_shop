from main.models import *


from django.db import models

from main.models import *



class Cart(models.Model):
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кол-во')
    color = models.ForeignKey(ProductImageColor, on_delete=models.CASCADE, verbose_name='Цвет товара')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = verbose_name
        unique_together = ("color",)

    def __str__(self):
        return str(self.color)
