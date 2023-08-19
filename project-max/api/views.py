from rest_framework import viewsets
from .serializer import OwnerSerializer
from .models import Owner
# Create your views here.

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer