from . import views
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import UserListAPIView, UserRetrieveUpdateDestroyAPIView

schema_view = get_schema_view(
   openapi.Info(
      title="Males Nugas API",
      default_version='v1',
      description="Males Nugas API for business",
      terms_of_service="https://www.yourapp.com/terms/",
      contact=openapi.Contact(email="fery.chaerul.ismail94@gmail.com"),
      license=openapi.License(name="Fery Ismail"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("test/", views.current_datetime, name='test'),
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]