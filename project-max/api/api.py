from .models import Owner,Especie,Raza,petSize,Pets,Vacuna,citaMedica
from rest_framework import viewsets, permissions
from .serializers import OwnerSerializer,EspecieSerializer,RazaSerializer,petSizeSerializer,PetsSerializer,VacunaSerializer,citaMedicaSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    permission_classes = [permissions.AllowAny] #Change to isAuthenticated
    serializer_class = OwnerSerializer

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    permission_classes = [permissions.AllowAny]  #Change to isAuthenticated
    serializer_class = EspecieSerializer

class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RazaSerializer

class petSizeViewSet(viewsets.ModelViewSet):
    queryset = petSize.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = petSizeSerializer

class PetsViewSet(viewsets.ModelViewSet):
    queryset = Pets.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PetsSerializer

class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VacunaSerializer

class citaMedicaViewSet(viewsets.ModelViewSet):
    queryset = citaMedica.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = citaMedicaSerializer