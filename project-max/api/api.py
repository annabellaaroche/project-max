from .models import Owner,Especie,Raza,petSize,Pets,Vacuna,citaMedica
from rest_framework import viewsets, permissions
from .serializers import OwnerSerializer,EspecieSerializer,RazaSerializer, VacunaSerializer2, citaMedicaSerializer2,petSizeSerializer,PetsSerializer,VacunaSerializer,citaMedicaSerializer
from .permissions import ReadOnlyOrAdminPermission
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False,methods=['GET'])
    def by_owner_id(self,request):
        owner_id= request.query_params.get('owner_id')
        if not owner_id:
            return Response({'error':'Por favor, proporciona un ID valido.'}, status=400)
        try:
            owner_id = int(owner_id)
        except ValueError:
            return Response({'error':'El ID debe ser un numero entero valido'}, status=400)
        
        pets = Pets.objects.filter(owner_id=owner_id)
        serializer = PetsSerializer(pets, many=True)
        return Response(serializer.data)
    
class VacunaViewSet(viewsets.ModelViewSet):
    queryset = Vacuna.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VacunaSerializer
        if self.request.method == 'POST':
            return VacunaSerializer2
        return VacunaSerializer2
    @action(detail=False,methods=['GET'])
    def by_owner_id(self,request):
        owner_id= request.query_params.get('owner_id')
        vacunas= Vacuna.objects.filter(mascota__owner_id=owner_id)
        serializer=VacunaSerializer(vacunas,many=True)
        return Response(serializer.data)

class citaMedicaViewSet(viewsets.ModelViewSet):
    queryset = citaMedica.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return citaMedicaSerializer
        if self.request.method == 'POST':
            return citaMedicaSerializer2
        return citaMedicaSerializer2
    
    @action(detail=False,methods=['GET'])
    def by_owner_id(self,request):
        owner_id= request.query_params.get('owner_id')
        citas= citaMedica.objects.filter(mascota__owner_id=owner_id)
        serializer=citaMedicaSerializer(citas,many=True)
        return Response(serializer.data)