from rest_framework import viewsets
from .models import ShoppingCart
from .serializers import ShopCartSerializer, ShopCartDetailSerializer


class ShoppingCartViewset(viewsets.ModelViewSet):
    serializer_class = ShopCartSerializer
    #  Мы изменяем идентификатор товара, а не идентификатор самой записи.
    lookup_field = "products_id"

    #  Компоненты шунтовой сериализации
    def get_serializer_class(self):
        if self.action == 'list':
            return ShopCartDetailSerializer
        else:
            return ShopCartSerializer

    def get_queryset(self):
        return ShoppingCart.objects.all()

