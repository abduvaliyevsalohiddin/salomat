from .serializers import *
from rest_framework.generics import *
from rest_framework.permissions import *
from .models import *
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class RegisterAPIView(CreateAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileRetrieveView(RetrieveAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileRetrieveUpdateDestroyView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        return self.request.user


class DoctorsListView(ListAPIView):
    serializer_class = ProfileSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="name",
                in_=openapi.IN_QUERY,
                description="Filter by full name (first or last name)",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                name="phone",
                in_=openapi.IN_QUERY,
                description="Filter by phone number",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                name="id",
                in_=openapi.IN_QUERY,
                description="Filter by doctor ID",
                type=openapi.TYPE_INTEGER,
            ),
        ],
    )
    def get(self, request):
        queryset = Profile.objects.filter(role='doctor')

        # Qidiruv parametrlarini olish
        name = self.request.query_params.get('name', None)
        fathers_name = self.request.query_params.get('fathers_name', None)
        phone = self.request.query_params.get('phone', None)
        doctor_id = self.request.query_params.get('id', None)

        if name:
            queryset = queryset.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name) | Q(fathers_name__icontains=name))

        if fathers_name:
            queryset = queryset.filter(fathers_name__icontains=fathers_name)

        if phone:
            queryset = queryset.filter(phone__icontains=phone)

        if doctor_id:
            queryset = queryset.filter(id=doctor_id)

        serializer = ProfileSerializer(queryset, many=True)

        return Response({
            'count': queryset.count(),
            'results': serializer.data
        }, status=status.HTTP_200_OK)
