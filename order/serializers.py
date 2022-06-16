#  порядок
from rest_framework import serializers

from cart.models import ShoppingCart
from cart.serializers import ShopCartSerializer
from cart.serializers import ProductSerializer
from main.models import Product, ProductImageColor, User
from order.models import Order
from main.serializers import ProductSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProductImageColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageColor
        fields = ('image', 'color')
        ref_name = 'Image'


class ProductSerializer(serializers.ModelSerializer):
    # images = ProductImageColorSerializer(many=True)
    title = serializers.CharField(source='products.title')
    id = serializers.IntegerField(source='products.id')
    # images = serializers.ImageField(source='products.image')

    class Meta:
        model = ShoppingCart
        fields = ('id', 'title')
        ref_name = 'ProductOrder'


class ProductDetaiSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='products.title')
    id = serializers.IntegerField(source='products.id')
    collection = serializers.CharField(source='products.collection')

    class Meta:
        model = ShoppingCart
        fields = ('id', 'title')
        ref_name = 'ProductOrder'


class OrderSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(
    #     default=serializers.CurrentUserDefault()
    # )
    #  Некоторая информация в заказе не может быть изменена самостоятельно
    order_sn = serializers.CharField(read_only=True)
    total_price = serializers.IntegerField(read_only=True)
    price_with_discount = serializers.IntegerField(read_only=True)
    discount = serializers.IntegerField(read_only=True)
    quantity_of_products = serializers.IntegerField(read_only=True)
    add_time = serializers.DateTimeField(read_only=True)

    # products = serializers.CharField(read_only=True)

    #  Функция создания номера заказа
    def generate_order_sn(self):
        #  Текущее время + случайное число
        from time import strftime
        from random import Random
        random_ins = Random()
        order_sn = "{time_str}{ranstr}".format(time_str=strftime("%Y%m%d%H%M%S"),
                                               # userid=self.context["request"].user.id,
                                               ranstr=random_ins.randint(10, 99))
        return order_sn

    #  Сгенерировать номер заказа
    def validate(self, attrs):
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)
        representation['products'] = ProductSerializer(instance.products, many=True).data
        return representation


#  Информация для заказа
class OrderDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def perform_create(self, serializer, *args, **kwargs):
        order = serializer.save()
        shop_carts = ShoppingCart.objects.all()
        for shop_cart in shop_carts:
            order_products = Order()
            order_products.products = shop_cart.products

            order_products.product_quantity = shop_cart.quantity
            order_products.save()
            shop_cart.delete()
        return order
