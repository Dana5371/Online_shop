from rest_framework import serializers

from main.models import *

#О нас
class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ('image',)

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        exclude = ('id',)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = AboutUsImageSerializer(instance.images.all(), many=True).data
        return representation


#Наши преимущества
class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'


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
        fields = ('name','number_of_phone')


#Товары
class ProductImageColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageColor
        fields = ('image', 'color')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('new', 'hit', 'id')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageColorSerializer(instance.images.all(), many=True).data
        return representation





