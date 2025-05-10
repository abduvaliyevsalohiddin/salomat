from django.contrib import admin
from django.urls import path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

from user.views import *
from main.views import *

from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

schema_view = get_schema_view(
    openapi.Info(
        title="Salomat API",
        default_version='v1',
        description="Test Salomat API",
        contact=openapi.Contact("Abduvaliyev Salohiddin. Email: abduvaliyevsalohiddin568@gmail.com")
    ),
    public=True,
    # permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Swagger
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),

    # Simple JWT
    path('token/', token_obtain_pair),
    path('token/refresh/', token_refresh),

    # User
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('profile/', ProfileRetrieveUpdateDestroyView.as_view()),
    path('profile/<int:pk>/', ProfileRetrieveView.as_view()),

    # Doctors
    path('doctors/', DoctorsListView.as_view()),

    # Orders
    path('orders/', OrderListCreateAPIView.as_view()),
    # path('order/<int:pk>/', OrderListAPIView.as_view()),

    # Recommendations
    path('recommendations/', RecommendationsListCreateAPIView.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
