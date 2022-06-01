from rest_framework import serializers

from main.models import *

class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = '__all__'

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
    
    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     images_data = request.FILES
    #     about_us = AboutUs.objects.create(**validated_data)
    #     for image in images_data.getlist('images'):
    #         AboutUsImage.objects.create(image=image, about_us=about_us)
    #     return about_us
    #
    # def update(self, instance, validated_data):
    #     request = self.context.get('request')
    #     for key, value in validated_data.items():
    #         setattr(instance, key, value)
    #     images_data = request.FILES
    #     instance.images.all().delete()
    #     for image in images_data.getlist('images'):
    #         AboutUsImage.objects.create(image=image, about_us = instance)
    #     return instance
    #
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['images'] = AboutUsImage(instance.images.all(), many=True).data
    #     return representation


class BenefitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefit
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class OferrroSerializer(serializers.Serializer):
    class Meta:
        model = Oferro
        fields = '__all__'

class ImageHelpSerializer(serializers.Serializer):
    class Meta:
        model = ImageHelp
        fields = '__all__'

class QuestionSerializer(serializers.Serializer):
    class Meta:
        model = Question
        fields = '__all__'



        