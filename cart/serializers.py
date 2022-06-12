from rest_framework import serializers

from cart.models import *
from main.models import *


class ProductSerializer(serializers.ModelSerializer):
    """Все продукты"""

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'discount', 'new_price', 'size')
        ref_name = 'ProductCart'


class ProductColorSerializer(serializers.ModelSerializer):
    """Цвета и фото товаров"""

    class Meta:
        model = ProductImageColor
        fields = ('color', 'image')


class ShopCartDetailSerializer(serializers.ModelSerializer):
    """Информация о продукте в корзине"""
    products = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ("color", 'quantity', 'products')



class ShopCartSerializer(serializers.Serializer):
    """Корзина"""
    quantity = serializers.IntegerField(required=True, label="Количество", min_value=1,
                                        error_messages={
                                            "min_value": "Количество товаров не может быть меньше одного",
                                            "required": "Пожалуйста, выберите количество покупок"
                                        })
    color = serializers.PrimaryKeyRelatedField(required=True, queryset=ProductImageColor.objects.all())
    #  Обработка внешнего ключа сериализатора должна использовать это поле, если это ModelSerializer
    #  также может использовать это поле, но не нужно указывать набор запросов
    products = serializers.PrimaryKeyRelatedField(required=True, queryset=Product.objects.all())

    def create(self, validated_data):
        print(validated_data)
        quantity = validated_data["quantity"]
        products = validated_data["products"]
        color = validated_data["color"]
        print(type(color))

        existed = ShoppingCart.objects.filter(products=products, color=color)

        #  Определите, есть ли в данный момент запись
        if existed:
            existed = existed[0]
            existed.quantity += quantity
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)
        #  Необходимо вернуться, чтобы сохранить данные
        return existed

    def update(self, instance, validated_data):
        #  Изменить количество товара
        instance.amount = validated_data["quantity"]
        instance.save()
        return instance
