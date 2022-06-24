from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
from rest_framework.filters import SearchFilter, OrderingFilter
import random

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .serializers import *


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
    pagination_class = FourAPIListPagination


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
        {
            'queryset': Help.objects.all(),
            'serializer_class': HelpSerializer
        },
        {
            'queryset': ImageHelp.objects.all(),
            'serializer_class': ImageHelpSerializer
        }
    ]


class CollectionMainPageListView(ListAPIView):
    """Коллекция для главной страницы"""
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    pagination_class = FourAPIListPagination


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


class ProductViewSet(mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    """Товар"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['title']
    pagination_class = TwelveAPIListPagination

    @action(detail=True, methods=['post'],
            permission_classes=[IsAuthenticated])
    def favorite(self, request, pk=None):
        products = self.get_object()
        obj, created = Favorite.objects.get_or_create(
            user=request.user, products=products)
        if not created:
            obj.favorite = not obj.favorite
            obj.save()
        favorites = 'added to favorites' if obj.favorite else 'removed to favorites'
        return Response(
            'Successfully {} !'.format(favorites), status=status.HTTP_200_OK)

    # если поиск не удался,вытаскиваем 5
    # рандомных продуктов из разных коллекций
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            queryset = set(Product.objects.values_list(
                'collection', flat=True))
            queryset = [random.choice(Product.objects.filter(
                collection=i)) for i in queryset]
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


class FavoriteListView(APIView):
    """Избранные"""

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = Favorite.objects.filter(user=request.user)
        queryset = (product.products for product in queryset)
        if len(list(Favorite.objects.filter(favorite=True))) > 0:
            serializer = ProductSerializer(queryset, many=True)
            return Response({
                "Количество избранных товаров": len(list(
                    Favorite.objects.filter(favorite=True))),
                "Избранные товары": serializer.data})
            # если нет избранных,вытаскиваем
            # рандомом 5 продуктов из разных коллекций
        else:
            queryset = set(Product.objects.values_list(
                'collection', flat=True))
            print(queryset)
            queryset = [random.choice(Product.objects.filter(
                collection=i)) for i in queryset]
            serializer = ProductSerializer(queryset, many=True)
        return Response({
            "Количество избранных товаров": len(list(
                Favorite.objects.filter(favorite=True))),
            "Рекомендации": serializer.data,
        })


class FooterListView(ObjectMultipleModelAPIView):
    """Футер"""
    pagination_class = LimitPagination
    querylist = [
        {
            'queryset': Footer.objects.all(),
            'serializer_class': FooterSerializer
        },
        {
            'queryset': SecondFooter.objects.all(),
            'serializer_class': SecondFooterSerializer
        },
    ]
