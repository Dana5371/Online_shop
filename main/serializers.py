from rest_framework import serializers

from main.models import *

#О нас
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


#Наши преимущества
class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'


#Новости
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


#Публичная оферта
class OferroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oferro
        fields = '__all__'


#Помощь
class ImageHelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageHelp
        fields = '__all__'

class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = '__all__'
#Коллекция
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'

#Cлайдер
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


#Обратный звонок
class BackCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackCall
        fields = '__all__'


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



