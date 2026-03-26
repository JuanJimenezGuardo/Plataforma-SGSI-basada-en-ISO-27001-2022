from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer
from apps.users.permissions import IsConsultantOrReadOnly

class CompanyViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestión de empresas.
    Consultores y Admin pueden crear/editar, todos pueden ver.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsConsultantOrReadOnly]
