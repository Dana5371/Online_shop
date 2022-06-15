from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from rest_framework.views import APIView

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


class AboutUsListView(ListAPIView):
    """О нас"""
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class BenefitListView(ListAPIView):
    """Наши преимущества"""
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer


class NewsListView(ListAPIView):
    """Новости"""
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = EightAPIListPagination


class OferroListView(ListAPIView):
    """Публичная оферта"""
    queryset = Oferro.objects.all()
    serializer_class = OferroSerializer


class ImageHelpListView(ListAPIView):
    """Фотография для помощи"""
    queryset = ImageHelp.objects.all()
    serializer_class = ImageHelpSerializer


class HelpListView(ListAPIView):
    """Помощь"""
    queryset = Help.objects.all()
    serializer_class = HelpSerializer


class CollectionListView(ListAPIView):
    """Коллекция"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = EightAPIListPagination


class CollectionProductDetailView(RetrieveAPIView):
    """Коллекция"""
    queryset = Collection.objects.all()
    serializer_class = CollectionProductSerializer
    pagination_class = TwelveAPIListPagination


class SliderListView(ListAPIView):
    """Слайдер"""
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class BackCallListView(APIView):
    """Обратный звонок"""

    # 1. List all
    def get(self):
        back = BackCall.objects.all()
        serializer = BackCallSerializer(back, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'name': request.data.get('name'),
            'number_of_phone': request.data.get('number_of_phone'),
            'status': request.data.get('status'),
        }
        serializer = BackCallPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class BackcallDeleteApi(DestroyAPIView):
    queryset = BackCall.objects.all()
    serializer_class = BackCallSerializer


class ProductListView(ListAPIView):
    """Товар"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['title']
    pagination_class = TwelveAPIListPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  # errorerror
        print(queryset)
        if not queryset:
            queryset = set(Product.objects.values_list('collection', flat=True))  ##errorerrrorrorororororo
            queryset = [random.choice(Product.objects.filter(collection=i)) for i in queryset]

        page = self.paginate_queryset(queryset)#erororororrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ProductDetailView(RetrieveAPIView):
    """Товар"""
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


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 8


# Главная страница
class MainPageListView(ObjectMultipleModelAPIView):
    pagination_class = LimitPagination
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


class FooterListView(ObjectMultipleModelAPIView):
    pagination_class = LimitPagination
    querylist = [
        {'queryset': Footer.objects.all(), 'serializer_class': FooterSerializer},
        {'queryset': SecondFooter.objects.all(), 'serializer_class': SecondFooterSerializer},
        {'queryset': Number.objects.all(), 'serializer_class': NumberSerializer},
    ]
