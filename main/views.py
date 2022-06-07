from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView

from .serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter
import random


# Классы пагинации
class EightAPIListPagination(PageNumberPagination):
    page_size = 8
    page_query_param = page_size
    max_page_size = 8


class FourAPIListPagination(PageNumberPagination):
    page_size = 4
    page_query_param = page_size
    max_page_size = 4


class TwelveAPIListPagination(PageNumberPagination):
    page_size = 12
    page_query_param = page_size
    max_page_size = 12


class FiveAPIListPagination(PageNumberPagination):
    page_size = 5
    page_query_param = page_size
    max_page_size = 5


# О нас
class AboutUsListView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


# Наши преимущества
class BenefitListView(ListAPIView):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer


# Новости
class NewsListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = EightAPIListPagination


# Публичная оферта
class OferroListView(ListAPIView):
    queryset = Oferro.objects.all()
    serializer_class = OferroSerializer


# Помощь
class ImageHelpListView(ListAPIView):
    queryset = ImageHelp.objects.all()
    serializer_class = ImageHelpSerializer


class HelpListView(ListAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer


# Коллекция
class CollectionListView(ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = EightAPIListPagination


class CollectionProductDetailView(RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionProductSerializer
    pagination_class = TwelveAPIListPagination


# Слайдер
class SliderListView(ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


# Обратный звонок
class BackCallListView(ListAPIView):
    queryset = BackCall.objects.all()
    serializer_class = BackCallSerializer


# Товары

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['title']
    pagination_class = TwelveAPIListPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        if not queryset:
            queryset = set(Product.objects.values_list('collection', flat=True))
            queryset = [random.choice(Product.objects.filter(collection=i)) for i in queryset]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


# Новинки
class NewListView(ListAPIView):
    queryset = Product.objects.filter(new=True)
    serializer_class = NewProductSerializer
    pagination_class = FiveAPIListPagination


# Хит продаж
class HitListView(ListAPIView):
    queryset = Product.objects.filter(hit=True)
    serializer_class = HitProductSerializer
    pagination_class = EightAPIListPagination


# Главная страница
class MainPageListView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Slider.objects.all(), 'serializer_class': SliderSerializer},
        {'queryset': Product.objects.filter(new=True)[:4], 'serializer_class': NewProductSerializer},
        {'queryset': Product.objects.filter(hit=True)[:8], 'serializer_class': HitProductSerializer},
        {'queryset': Collection.objects.all()[:4], 'serializer_class': CollectionSerializer},
        {'queryset': Benefit.objects.all()[:4], 'serializer_class': BenefitSerializer}
    ]


class FavoriteListView(ListAPIView):
    queryset = Product.objects.filter(favorite=True)
    serializer_class = FavoriteSerializer
    pagination_class = TwelveAPIListPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            queryset = set(Product.objects.values_list('collection', flat=True))
            queryset = [random.choice(Product.objects.filter(collection=i)) for i in queryset]

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
