import random

from django.db.models import Q
from rest_framework import serializers

from main.models import *


# О нас
class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ('image',)


class AboutUsSerializer(serializers.ModelSerializer):
    images = AboutUsImageSerializer(many=True)

    class Meta:
        model = AboutUs
        fields = ('title', 'text', 'images')


# Наши преимущества
class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = ('icon', 'title', 'description')


# Новости
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'description', 'image')


# Публичная оферта
class OferroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferro
        fields = ('title', 'description')


# Помощь
class ImageHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageHelp
        fields = '__all__'


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = '__all__'


# Коллекция
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'image', 'title')


# Cлайдер
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


# Обратный звонок
class BackCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackCall
        fields = ('name', 'number_of_phone')


# Товары
class ProductImageColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageColor
        fields = ('image', 'color')


# Похожие товары
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('collection', 'title', 'article', 'old_price', 'discount', 'new_price',
                  'description', 'size', 'line_of_size', 'compound', 'amount', 'material', 'favorite', 'images')


class SimilarProductSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'discount', 'new_price',
                  'size', 'favorite', 'images')


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)
    similar = serializers.SerializerMethodField('get_similar_product')

    class Meta:
        model = Product
        fields = ('collection', 'title', 'article', 'old_price', 'discount', 'new_price',
                  'description', 'size', 'line_of_size', 'compound', 'amount', 'material', 'favorite', 'images',
                  'similar')

    def get_similar_product(self, obj):
        similar = Product.objects.filter(Q(collection=obj.collection) & ~Q(id=obj.id))[:5]
        similar_data = SimilarProductSerializer(similar, many=True)
        return similar_data.data


# Детализация коллекции
class CollectionProductSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField('get_products')

    class Meta:
        model = Collection
        fields = ('id', 'image', 'title', 'products')

    def get_products(self, obj):
        products = Product.objects.filter(collection=obj.id)
        products_data = ProductSerializer(products, many=True)
        return products_data.data


# Новинки
class NewProductSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'new_price', 'discount', 'size', 'favorite', 'images')


# Хит продаж
class HitProductSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'new_price', 'discount', 'size', 'favorite', 'images')


class FavoriteSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)
    count_favorite = serializers.SerializerMethodField('get_favorite_count')

    class Meta:
        model = Product
        fields = ('id', 'discount', 'old_price', 'new_price', 'title', 'size', 'favorite', 'images', 'count_favorite')

    def get_favorite_count(self, obj):
        count_fav = Product.objects.filter(favorite=True)
        count_fav_data = ProductSerializer(count_fav, many=True)
        return len(count_fav_data.data)


class NumberSerializer(serializers.Serializer):
    class Meta:
        model = Number
        fields = ('number')


class SecondFooter(serializers.ModelSerializer):
    number = NumberSerializer(many=True)

    class Meta:
        model = SecondFooter
        fields = ('number', 'logo',)
