from rest_framework import viewsets

from .models import Cart
from .serializers import ShopCartSerializer, ShopCartDetailSerializer


class ShoppingCartViewset(viewsets.ModelViewSet):
    serializer_class = ShopCartSerializer
    """изменяем идентификатор товара, а не идентификатор самой записи"""
    lookup_field = "color_id"

    def get_serializer_class(self):
        if self.action == 'list':
            return ShopCartDetailSerializer
        else:
            return ShopCartSerializer

    def get_queryset(self):
        return Cart.objects.all()

