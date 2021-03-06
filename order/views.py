from rest_framework import mixins, viewsets

from order.models import Order
from order.serializers import OrderSerializer, OrderDetailSerializer
from cart.models import Cart


class OrderViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                   mixins.CreateModelMixin, mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return OrderDetailSerializer
        return OrderSerializer

    def perform_create(self, serializer, *args, **kwargs):
        order = serializer.save()
        shop_carts = Cart.objects.all()
        for shop_cart in shop_carts:
            order_products = Order()
            # order_products.products = shop_cart.color
            order_products.product_quantity = shop_cart.quantity
            order_products.save()
            shop_cart.delete()
        return order
