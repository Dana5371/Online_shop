from rest_framework import viewsets
from .models import ShoppingCart
from .serializers import ShopCartSerializer, ShopCartDetailSerializer


# class AddToCart(APIView):
#     def post(self, request, product_id, format=None):
#         cart = Cart(request)
#         product = get_object_or_404(Product, id=product_id)
#         color_of_product = request.data.get('color').upper()
#         color = get_object_or_404(ProductImageColor, color=color_of_product, products=product)
#         print('hello'),
#         print(color)
#         cart.add(product, color)
#         return Response({"status" : "Успешно"})
#
# class GetCart(APIView):
#     def get(self, request, format=None):
#         cart = Cart(request)
#         # получаем все товары из корзины пользователя в виде обьектов
#         products_cart = cart.get_product()
#         color = products_cart['color']
#         serial = CartSerializer(color, many=True, context = cart.cart)
#         return Response(serial.data)
#
# class CartRemove(APIView):
#     def post(self, request, pk):
#         cart = Cart(request)
#         product = get_object_or_404(ProductImageColor, id=pk)
#         try:
#             color_object = request.data.get('product_color').upper()
#         except AttributeError:
#             return Response({"message": "product_color is required"})
#         minus = request.data.get('minus')
#         # получаем обьект цвета товара
#         color = get_object_or_404(ProductImageColor, color=color_object, image_color=product)
#         cart.remove(color=color, minus=minus)
#         return Response({"status": "success"})
#
# class ClearCart(APIView):
#     def get(self, request, format=None):
#         cart = Cart(request)
#         cart.clear()
#         return Response({"status": "clear"})

class ShoppingCartViewset(viewsets.ModelViewSet):
    """
    list:
                 Получить информацию о корзине покупок
    create：
                 добавить в корзину
    delete：
                 Удалить запись о покупках
    """

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
