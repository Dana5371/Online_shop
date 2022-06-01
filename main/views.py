from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.

class AboutUsViewSet(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer

class BenefitViewSet(ModelViewSet):
    queryset = Benefit.objects.all()
    serializer_class = BenefitSerializer

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

