from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


#О нас
class AboutUsViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


#Наши преимущества
class BenefitViewSet(ModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer


#Новости
class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


#Публичная оферта
class OferroViewSet(ModelViewSet):
    queryset = Oferro.objects.all()
    serializer_class = OferrroSerializer


#Помощь
class ImageHelpViewSet(ModelViewSet):
    queryset = ImageHelp.objects.all()
    serializer_class = ImageHelpSerializer

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

#Коллекция
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
