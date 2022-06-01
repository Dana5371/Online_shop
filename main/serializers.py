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
class OferrroSerializer(serializers.Serializer):
    class Meta:
        model = Oferro
        fields = '__all__'


#Помощь
class ImageHelpSerializer(serializers.Serializer):
    class Meta:
        model = ImageHelp
        fields = '__all__'

class QuestionSerializer(serializers.Serializer):
    class Meta:
        model = Question
        fields = '__all__'


#Коллекция
class CollectionSerializer(serializers.Serializer):
    class Meta:
        model = Collection
        fields = '__all__'
