from django.db.models import Q
from rest_framework import serializers

from main.models import *


class AboutUsImageSerializer(serializers.ModelSerializer):
    """О нас фотографии"""

    class Meta:
        model = AboutUsImage
        fields = ('image',)


class AboutUsSerializer(serializers.ModelSerializer):
    """О нас"""
    images = AboutUsImageSerializer(many=True)

    class Meta:
        model = AboutUs
        fields = ('title', 'text', 'images')


class BenefitSerializer(serializers.ModelSerializer):
    """Наши преимущества"""

    class Meta:
        model = Benefit
        fields = ('icon', 'title', 'description')


class NewsSerializer(serializers.ModelSerializer):
    """Новости"""

    class Meta:
        model = News
        fields = ('title', 'description', 'image')


class OferroSerializer(serializers.ModelSerializer):
    """Публичная оферта"""

    class Meta:
        model = Oferro
        fields = ('title', 'description')


class ImageHelpSerializer(serializers.ModelSerializer):
    """Фотография для помощи"""

    class Meta:
        model = ImageHelp
        fields = '__all__'


class HelpSerializer(serializers.ModelSerializer):
    """Помощь"""

    class Meta:
        model = Help
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    """Коллекция"""

    class Meta:
        model = Collection
        fields = ('id', 'image', 'title')


class SliderSerializer(serializers.ModelSerializer):
    """Слайдер"""

    class Meta:
        model = Slider
        fields = '__all__'


class BackCallSerializer(serializers.ModelSerializer):
    """Обратный звонок"""

    class Meta:
        model = BackCall
        fields = ('id', 'name', 'number_of_phone', 'type')


class ProductImageColorSerializer(serializers.ModelSerializer):
    """Фотография и цвет для товара"""

    class Meta:
        model = ProductImageColor
        fields = ('image', 'color')


class ProductSerializer(serializers.ModelSerializer):
    """Товар"""
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('collection', 'title', 'article', 'old_price',
                  'discount', 'new_price', 'description', 'size',
                  'line_of_size', 'compound', 'material',
                  'images')


class SimilarProductSerializer(serializers.ModelSerializer):
    """Похожие товары"""
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'discount', 'new_price',
                  'size','images')


class ProductDetailSerializer(serializers.ModelSerializer):
    """Детализация товара"""
    images = ProductImageColorSerializer(many=True)
    alike = serializers.SerializerMethodField('get_alike_product')

    class Meta:
        model = Product
        fields = ('collection', 'title', 'article', 'old_price',
                  'discount', 'new_price', 'description', 'size',
                  'line_of_size', 'compound', 'material',
                  'images', 'alike')

    def get_alike_product(self, obj):
        alike = Product.objects.filter(
            Q(collection=obj.collection) & ~Q(id=obj.id))[:5]
        alike_data = SimilarProductSerializer(alike, many=True).data
        return alike_data


class CollectionProductSerializer(serializers.ModelSerializer):
    """Детализация коллекции"""
    products = serializers.SerializerMethodField('get_products')
    new_products = serializers.SerializerMethodField('get_new_product')

    class Meta:
        model = Collection
        fields = ('id', 'image', 'title', 'products', 'new_products')

    def get_products(self, obj):
        products = Product.objects.filter(collection=obj.id)
        products_data = ProductSerializer(products, many=True)
        return products_data.data

    def get_new_product(self, obj):
        products = Product.objects.filter(new=True)[:5]
        products_data = ProductSerializer(products, many=True)
        return products_data.data


class NewProductSerializer(serializers.ModelSerializer):
    """Новинки"""
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'new_price',
                  'discount', 'size','images')


class HitProductSerializer(serializers.ModelSerializer):
    """Хит продаж"""
    images = ProductImageColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'new_price',
                  'discount', 'size', 'images')


# class FavoriteSerializer(serializers.ModelSerializer):
#     """Избранные"""
#     images = ProductImageColorSerializer(many=True)
#
#     class Meta:
#         model = Product
#         fields = ('id', 'discount', 'old_price', 'new_price',
#                   'title', 'size','images')


class FooterSerializer(serializers.ModelSerializer):
    """Футер"""

    class Meta:
        model = Footer
        fields = ('logo', 'imformation', 'number')


class SecondFooterSerializer(serializers.ModelSerializer):
    """Футер вторая вкладка"""

    class Meta:
        model = SecondFooter
        fields = ('messen', 'link')


class FavoriteUserSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='products.title')
    collection = serializers.CharField(source='products.collection')
    old_price = serializers.CharField(source='products.old_price')
    new_price = serializers.CharField(source='products.new_price')
    discount = serializers.CharField(source='products.discount')
    size = serializers.CharField(source='products.size')
    line = serializers.CharField(source='products.line_of_size')

    class Meta:
        model = Favorite
        fields = ('favorite', 'user', 'favorite', 'title', 'collection',
                  'old_price', 'new_price', 'discount', 'size', 'line')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.email
        representation['products'] = instance.products.title
        return representation