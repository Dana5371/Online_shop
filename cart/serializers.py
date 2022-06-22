from rest_framework import serializers

from .models import *


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageColor
        fields = ('image', 'color')


class ProductSerializer(serializers.ModelSerializer):
    images = ProductColorSerializer(many=True)
    """Все продукты"""

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price',
                  'discount', 'new_price',
                  'size', 'images')
        ref_name = 'ProductCart'


class ShopCartDetailSerializer(serializers.ModelSerializer):
    """Информация о продукте в корзине"""
    title = serializers.CharField(source='color.products.title')
    image = serializers.CharField(source='color.image')

    class Meta:
        model = Cart
        fields = ("color", "quantity", 'title', 'image')


class ShopCartSerializer(serializers.Serializer):
    title = serializers.CharField(source='color.products.title',
                                  read_only=True)
    collection = serializers.CharField(source='color.products.collection',
                                       read_only=True)
    old_price = serializers.CharField(source='color.products.old_price',
                                      read_only=True)
    new_price = serializers.CharField(source='color.products.new_price',
                                      read_only=True)
    discount = serializers.CharField(source='color.products.discount',
                                     read_only=True)
    size = serializers.CharField(source='color.products.size', read_only=True)
    line = serializers.CharField(source='color.products.line_of_size',
                                 read_only=True)
    image = serializers.CharField(source='color.image', read_only=True)
    color_code = serializers.CharField(source='color.color', read_only=True)

    """корзина"""
    quantity = serializers.IntegerField(required=True, label="Количество",
                                        min_value=1,
                                        error_messages={
                                            "min_value":
                                                "Количество товаров не < 1",
                                            "required":
                                                "Выберите количество покупок"
                                        })
    """Обработка внешнего ключа сериализатора должна
    использовать это поле, если это ModelSerializer
    также может использовать это поле, но не нужно
    указывать набор запросов"""
    color = serializers.PrimaryKeyRelatedField(
        required=True,
        queryset=ProductImageColor.objects.all())

    def create(self, validated_data):
        print(validated_data)
        quantity = validated_data["quantity"]
        color = validated_data["color"]

        existed = Cart.objects.filter(color=color)

        #  Проверка на наличие запися GET
        if existed:
            existed = existed[0]
            existed.quantity += quantity
            existed.save()
        else:
            existed = Cart.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        """Для изменения кол-во товара"""
        instance.quantity = validated_data["quantity"]
        instance.save()
        return instance
