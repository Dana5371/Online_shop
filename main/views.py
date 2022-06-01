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

class OferroViewSet(ModelViewSet):
    queryset = Oferro.objects.all()
    serializer_class = OferrroSerializer

class ImageHelpViewSet(ModelViewSet):
    queryset = ImageHelp.objects.all()
    serializer_class = ImageHelpSerializer

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
