from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .models import *
from .serializers import *

#Классы пагинации
class EightAPIListPagination(PageNumberPagination):
    page_size = 8
    page_query_param = page_size
    max_page_size = 10

class TwelveAPIListPagination(PageNumberPagination):
    page_size = 12
    page_query_param = page_size
    max_page_size = 12

class FiveAPIListPagination(PageNumberPagination):
    page_size = 5
    page_query_param = page_size
    max_page_size = 5

#О нас
class AboutUsListView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


#Наши преимущества
class BenefitListView(generics.ListAPIView):
    queryset = Benefit
    serializer_class = BenefitSerializer


#Новости
class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = EightAPIListPagination


#Публичная оферта
class OferroListView(generics.ListAPIView):
    queryset = Oferro
    serializer_class = OferroSerializer


#Помощь
class ImageHelpListView(generics.ListAPIView):
    queryset = ImageHelp
    serializer_class = ImageHelpSerializer

class HelpListView(generics.ListAPIView):
    queryset = Help
    serializer_class = HelpSerializer

#Коллекция
class CollectionListView(generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = EightAPIListPagination

class CollectionProductDetailView(generics.RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionProductSerializer
    pagination_class = TwelveAPIListPagination


#Слайдер
class SliderListView(generics.ListAPIView):
    queryset = Slider
    serializer_class = SliderSerializer


#Обратный звонок
class BackCallListView(generics.ListAPIView):
    queryset = BackCall
    serializer_class = BackCallSerializer


#Товары
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = TwelveAPIListPagination


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#Новинки
class NewListView(generics.ListAPIView):
    queryset = Product.objects.filter(new=True)
    serializer_class = NewProductSerializer
    pagination_class = FiveAPIListPagination

#Хит продаж
class HitListView(generics.ListAPIView):
    queryset = Product.objects.filter(hit=True)
    serializer_class = HitProductSerializer
    pagination_class = EightAPIListPagination

#Главная страница
class MainPageListView(generics.ListAPIView):
    queryset = Product.objects.filter(hit=True)
    serializer_class = MainPageSerializer









