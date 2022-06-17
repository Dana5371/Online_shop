from rest_framework import serializers

from cart.models import *
from main.models import *


class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageColor
        fields = ('image', 'color')


class ProductSerializer(serializers.ModelSerializer):
    images = ProductColorSerializer(many=True)
    """Все продукты"""

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'discount', 'new_price', 'size', 'images')
        ref_name = 'ProductCart'


class ShopCartDetailSerializer(serializers.ModelSerializer):
    """Информация о продукте в корзине"""
    products = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ("products", "quantity")


class ShopCartSerializer(serializers.Serializer):
    """корзина"""
    quantity = serializers.IntegerField(required=True, label="Количество", min_value=1,
                                        error_messages={
                                            "min_value": "Количество товаров не может быть меньше одного",
                                            "required": "Пожалуйста, выберите количество покупок"
                                        })
    """Обработка внешнего ключа сериализатора должна использовать это поле, если это ModelSerializer также 
    может использовать это поле, но не нужно указывать набор запросов"""
    products = serializers.PrimaryKeyRelatedField(required=True, queryset=Product.objects.all())

    def create(self, validated_data):
        quantity = validated_data["quantity"]
        products = validated_data["products"]

        existed = ShoppingCart.objects.filter(products=products)

        #  Проверка на наличие запися
        if existed:
            existed = existed[0]
            existed.quantity += quantity
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)

        return existed

    def update(self, instance, validated_data):
        """Для изменения кол-во товара"""
        instance.quantity = validated_data["quantity"]
        instance.save()
        return instance
