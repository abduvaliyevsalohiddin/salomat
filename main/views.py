from .models import *
from .serializers import *
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import *
from rest_framework.permissions import *


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'doctor':
            return Order.objects.filter(doctor=user)
        elif user.role == 'patient':
            return Order.objects.filter(patient=user)
        else:
            raise PermissionDenied("Faqat doktorlar yoki bemorlar buyurtmalarni ko‘ra oladi.")

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'patient':
            raise PermissionDenied("Faqat bemorlar buyurtma yaratishi mumkin.")
        doctor_id = self.request.data.get('doctor')
        if not doctor_id:
            raise serializers.ValidationError({"doctor": "Doktor ID talab qilinadi."})
        serializer.save(patient=user)


class RecommendationsListCreateAPIView(ListCreateAPIView):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationsSerializer

    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'doctor':
            raise PermissionDenied("Faqat doktorlar tavsiyalarni yaratishi mumkin.")

        # Tavsiya yaratish uchun doctorni qo'shamiz
        serializer.save(doctor=user)

    def get_queryset(self):
        user = self.request.user

        # Agar foydalanuvchi bemor bo'lsa, faqat o'ziga tegishli tavsiyalarni ko'rishi mumkin
        if user.role == 'patient':
            return Recommendations.objects.filter(patient=user)

        # Agar foydalanuvchi doktor bo'lsa, faqat o'ziga tegishli bemorlarning tavsiyalarini ko'rishi mumkin
        elif user.role == 'doctor':
            return Recommendations.objects.filter(doctor=user)

        # Agar foydalanuvchi rolini aniqlay olmasak, ruxsat berilmaydi
        else:
            raise PermissionDenied("Foydalanuvchi tavsiyalarni ko‘ra olmaydi.")
