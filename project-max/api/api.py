from .models import Owner,Especie,Raza,petSize,Pets,Vacuna,citaMedica
from rest_framework import viewsets, permissions
from .serializers import OwnerSerializer,EspecieSerializer,RazaSerializer, VacunaSerializer2, citaMedicaSerializer2,petSizeSerializer,PetsSerializer,VacunaSerializer,citaMedicaSerializer
from .permissions import ReadOnlyOrAdminPermission
class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    permission_classes = [permissions.IsAuthenticated] #Change to isAuthenticated
    serializer_class = OwnerSerializer

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    permission_classes = [permissions.IsAdminUser]  #Change to isAuthenticated
    serializer_class = EspecieSerializer

class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()
    permission_classes = [ReadOnlyOrAdminPermission]
    serializer_class = RazaSerializer

class petSizeViewSet(viewsets.ModelViewSet):
    queryset = petSize.objects.all()
    permission_classes = [ ReadOnlyOrAdminPermission]
    serializer_class = petSizeSerializer

class PetsViewSet(viewsets.ModelViewSet):
    queryset = Pets.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PetsSerializer

class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VacunaSerializer
        if self.request.method == 'POST':
            return VacunaSerializer2
        return VacunaSerializer2

class citaMedicaViewSet(viewsets.ModelViewSet):
    queryset = citaMedica.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return citaMedicaSerializer
        if self.request.method == 'POST':
            return citaMedicaSerializer2
        return citaMedicaSerializer2