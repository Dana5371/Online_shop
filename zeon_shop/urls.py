"""zeon_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

from account.views import RegisterView
from cart.views import *
from order.views import OrderViewset

from main.views import *
from main import views

schema_view = get_schema_view(
    openapi.Info(
        title="ZEON_SHOP",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'cart', ShoppingCartViewset, basename="cart")
router.register(r'order', OrderViewset, basename="order")
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui()),
    path('api/v1/about-us/', AboutUsListView.as_view()),
    path('api/v1/benefit/', BenefitListView.as_view()),
    path('api/v1/news/', NewsListView.as_view()),
    path('api/v1/oferro/', OferroListView.as_view()),
    path('api/v1/help/', HelpListView.as_view()),
    path('api/v1/collection/', CollectionListView.as_view()),
    path('api/v1/backcall', BackCallListView.as_view()),
    path('api/v1/backcall/<int:pk>', BackcallDeleteApi.as_view()),
    path('api/v1/slider/', SliderListView.as_view()),
    path('api/v1/product/<str:pk>/', ProductDetailView.as_view()),
    path('api/v1/hit/', HitListView.as_view()),
    path('api/v1/new/', NewListView.as_view()),
    path('api/v1/favorite/', FavoriteListView.as_view()),
    path('api/v1/footer/', FooterListView.as_view()),
    path('api/v1/', include(router.urls)),
    path('api/v1/register/', RegisterView.as_view()),
    path('api/v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
