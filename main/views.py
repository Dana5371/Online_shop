"""Модули"""
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
import random

"""Импорты"""

from .serializers import *

"""Классы пагинации"""


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 8


class EightAPIListPagination(PageNumberPagination):
    page_size = 8


class FourAPIListPagination(PageNumberPagination):
    page_size = 4


class TwelveAPIListPagination(PageNumberPagination):
    page_size = 12


class FiveAPIListPagination(PageNumberPagination):
    page_size = 5


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


class HelpListView(ObjectMultipleModelAPIView):
    """Помощь"""
    pagination_class = LimitPagination
    querylist = [
        {'queryset': Help.objects.all(), 'serializer_class': HelpSerializer},
        {'queryset': ImageHelp.objects.all(), 'serializer_class': ImageHelpSerializer}
    ]


class CollectionListView(ListAPIView):
    """Коллекция"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = EightAPIListPagination


class CollectionProductDetailView(RetrieveAPIView):
    """Детализация коллекции"""
    queryset = Collection.objects.all()
    serializer_class = CollectionProductSerializer
    pagination_class = TwelveAPIListPagination


class SliderListView(ListAPIView):
    """Слайдер"""
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class BackCallListView(ListCreateAPIView):
    """Обратный звонок"""
    queryset = BackCall.objects.all()
    serializer_class = BackCallSerializer


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

    # если поиск не удался,вытаскиваем 5 рандомных продуктов из разных коллекций
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


class ProductDetailView(RetrieveAPIView):
    """Товар"""
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class NewListView(ListAPIView):
    """Новинки"""
    queryset = Product.objects.filter(new=True)
    serializer_class = NewProductSerializer
    pagination_class = FourAPIListPagination


class HitListView(ListAPIView):
    """Хит продаж"""
    queryset = Product.objects.filter(hit=True)
    serializer_class = HitProductSerializer
    pagination_class = EightAPIListPagination


class FavoriteListView(ListAPIView):
    """Избранные"""
    queryset = Product.objects.filter(favorite=True)
    serializer_class = FavoriteSerializer
    pagination_class = TwelveAPIListPagination

    # если нет избранных,вытаскиваем рандомом 5 продуктов из разных коллекций
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
    """Футер"""
    pagination_class = LimitPagination
    querylist = [
        {'queryset': Footer.objects.all(), 'serializer_class': FooterSerializer},
        {'queryset': SecondFooter.objects.all(), 'serializer_class': SecondFooterSerializer},
        {'queryset': Number.objects.all(), 'serializer_class': NumberSerializer},
    ]
