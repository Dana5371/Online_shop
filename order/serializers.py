from rest_framework import serializers

from cart.models import Cart
from cart.serializers import ProductSerializer
from main.models import ProductImageColor
from .models import Order


# from product.serializers import ProductSerializer


class ProductImageColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageColor
        fields = ('image', 'color')
        ref_name = 'Image'


class ProductSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='color.products.title')
    id = serializers.IntegerField(source='color.products.id')

    class Meta:
        model = Cart
        fields = ('id', 'title')
        ref_name = 'ProductOrder'


class ProductDetailSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='color.products.title')
    id = serializers.IntegerField(source='color.products.id')
    collection = serializers.CharField(source='color.products.collection')
    old_price = serializers.CharField(source='color.products.old_price')
    new_price = serializers.CharField(source='color.products.new_price')
    discount = serializers.CharField(source='color.products.discount')
    size = serializers.CharField(source='color.products.size')
    line = serializers.CharField(source='color.products.line_of_size')

    class Meta:
        model = Cart
        fields = ('color','title', 'collection', 'old_price', 'new_prce' 'discount', 'size', 'line')
        ref_name = 'ProductOrder'


class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField('get_product')
    """Некоторая информация в заказе не может быть изменена самостоятельно"""
    order_sn = serializers.CharField(read_only=True)
    total_price = serializers.IntegerField(read_only=True)
    price_with_discount = serializers.IntegerField(read_only=True)
    discount = serializers.IntegerField(read_only=True)
    quantity_of_products = serializers.IntegerField(read_only=True)
    add_time = serializers.DateTimeField(read_only=True)

    """Функция создания номера заказа"""

    def generate_order_sn(self):
        #  Текущее время + случайное число
        from time import strftime
        from random import Random
        random_ins = Random()
        order_sn = "{time_str}{ranstr}".format(time_str=strftime("%Y%m%d%H%M%S"),
                                               ranstr=random_ins.randint(10, 99))
        return order_sn

    """Сгенерировать номер заказа"""

    def validate(self, attrs):
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    class Meta:
        model = Order
        fields = "__all__"

    def get_product(self, obj):
        count_fav = Cart.objects.all()
        count_fav_data = ProductSerializer(count_fav, many=True)
        return count_fav_data.data


class OrderDetailSerializer(serializers.ModelSerializer):
    """Информация для заказа"""
    products = serializers.SerializerMethodField('get_product')

    class Meta:
        model = Order
        fields = '__all__'

    def get_product(self, obj):
        count_fav = Cart.objects.all()
        count_fav_data = ProductDetailSerializer(count_fav, many=True)
        return count_fav_data.data

    def perform_create(self, serializer, *args, **kwargs):
        order = serializer.save()
        shop_carts = Cart.objects.all()
        for shop_cart in shop_carts:
            order_products = Order()
            order_products.product_quantity = shop_cart.quantity
            order_products.save()
            shop_cart.delete()
        return order
