from main.models import *


class ShoppingCart(models.Model):
    products = models.ForeignKey(Product, verbose_name=u"товар", on_delete=models.CASCADE)
    color = models.ForeignKey(ProductImageColor, verbose_name=u"цвет и фото", on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(blank=True, null=True, verbose_name='Кол-во')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"добавить время")

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = verbose_name
        unique_together = ('color',)  # Товар не должен повторяться в корзине.

    def __str__(self):
        return str(self.products.title)
