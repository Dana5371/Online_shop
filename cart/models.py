from main.models import *


class ShoppingCart(models.Model):
    products = models.ForeignKey(Product, verbose_name=u"товар", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, verbose_name="Количество покупок")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"добавить время")

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = verbose_name
        unique_together = ("products",)  #  Товар не должен повторяться в корзине.

    def __str__(self):
        return f'{self.products.title} --> {self.quantity}'
