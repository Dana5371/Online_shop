from django.db.models import Q
from rest_framework import serializers

from main.models import *

#О нас
class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ('image',)

class AboutUsSerializer(serializers.ModelSerializer):
    images = AboutUsImageSerializer(many=True)
    class Meta:
        model = AboutUs
        fields = ('title', 'text', 'images')


#Наши преимущества
class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = ('icon', 'title', 'description')


#Новости
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title', 'description', 'image')


#Публичная оферта
class OferroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferro
        fields = ('title', 'description')


#Помощь
class ImageHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageHelp
        fields = '__all__'

class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = '__all__'

    def to_representation(self, instance):
        representetion = super.to_representetion(instance)
        representetion['images'] = ImageHelpSerializer(instance.images.all()).data
        return representetion
#Коллекция
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ('id', 'image', 'title')


#Cлайдер
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


#Обратный звонок
class BackCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackCall
        fields = ('name', 'number_of_phone')


#Товары
class ProductImageColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageColor
        fields = ('image', 'color')

#Похожие товары
class SimilarProductSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'discount', 'new_price',
                  'size','favorite', 'images')

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)
    similar = serializers.SerializerMethodField('get_similar_product')
    class Meta:
        model = Product
        fields = ('collection', 'title', 'article', 'old_price', 'discount', 'new_price',
                  'description', 'size', 'line_of_size','compound', 'amount','material', 'favorite','images' ,'similar')

    def get_similar_product(self, obj):
        similar = Product.objects.filter(Q(collection=obj.collection) & ~Q(id=obj.id))[:5]
        similar_data = SimilarProductSerializer(similar, many=True)
        return similar_data.data

#Детализация коллекции
class CollectionProductSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Collection
        fields = ('id', 'image', 'title', 'products')

#Новинки
class NewProductSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'new_price', 'discount', 'size', 'favorite', 'images' )


#Хит продаж
class HitProductSerializer(serializers.ModelSerializer):
    images = ProductImageColorSerializer(many=True)
    class Meta:
        model = Product
        fields = ('id', 'title', 'old_price', 'new_price', 'discount', 'size', 'favorite', 'images')



#Главная страница
class MainPageSerializer(serializers.Serializer):
    slider = serializers.SerializerMethodField('get_slider')
    new_products = serializers.SerializerMethodField('get_new_product')
    hit_products = serializers.SerializerMethodField('get_hit_product')
    collection = serializers.SerializerMethodField('get_collection')
    benefits = serializers.SerializerMethodField('get_benefit')

    def get_slider(self, obj):
        slider = Slider.objects.all()
        slider_data = SliderSerializer(slider, many=True)
        return slider_data.data

    def get_new_product(self, obj):
        new = Product.objects.filter(new=True)[:4]
        new_data = NewProductSerializer(new, many=True)
        return new_data.data

    def get_hit_product(self, obj):
        hit = Product.objects.filter(hit=True)[:8]
        hit_data = HitProductSerializer(hit, many=True)
        return hit_data.data

    def get_collection(self, obj):
        collection = Collection.objects.all()[:4]
        collection_data = CollectionSerializer(collection, many=True)
        return collection_data.data

    def get_benefit(self, obj):
        benefit = Benefit.objects.all()[:4]
        benefit_data = BenefitSerializer(benefit, many=True)
        return benefit_data.data




















