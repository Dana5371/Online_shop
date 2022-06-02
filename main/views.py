from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import *
from .serializers import *


#О нас
class AboutUsListView(APIView):

    def get(self, request):
            about_us = AboutUs.objects.all()
            serializer = AboutUsSerializer(about_us, many=True)
            return Response(serializer.data)


#Наши преимущества
class BenefitListView(APIView):

    def get(self, request):
            benefit = Benefit.objects.all()
            serializer = BenefitSerializer(benefit, many=True)
            return Response(serializer.data)


#Новости
class EightAPIListPagination(PageNumberPagination):
    page_size = 8
    page_query_param = page_size
    max_page_size = 10

class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = EightAPIListPagination


#Публичная оферта
class OferroListView(APIView):
    def get(self, request):
            oferro = Oferro.objects.all()
            serializer = OferroSerializer(oferro, many=True)
            return Response(serializer.data)

#Помощь
class ImageHelpListView(APIView):
    def get(self, request):
            imagehelp = ImageHelp.objects.all()
            serializer = ImageHelpSerializer(imagehelp, many=True)
            return Response(serializer.data)

class HelpListView(APIView):
    def get(self, request):
            help = Help.objects.all()
            serializer = HelpSerializer(help, many=True)
            return Response(serializer.data)

#Коллекция
class CollectionListView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = EightAPIListPagination


#Слайдер
class SliderListView(APIView):
    def get(self, request):
            slider = Slider.objects.all()
            serializer = SliderSerializer(slider, many=True)
            return Response(serializer.data)

#Обратный звонок
class BackCallListView(APIView):

    def get(self, request):
            back_call = BackCall.objects.all()
            serializer = BackCallSerializer(back_call, many=True)
            return Response(serializer.data)

#Товары
class ProductListView(APIView):

    def get(self, request):
            product = Product.objects.all()
            serializer = ProductSerializer(product, many=True)
            return Response(serializer.data)

@api_view(['GET'])
def ProductDetail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)





