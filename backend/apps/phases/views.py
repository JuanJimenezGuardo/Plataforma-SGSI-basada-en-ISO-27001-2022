from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Phase
from .serializers import PhaseSerializer

class PhaseViewSet(viewsets.ModelViewSet):
    queryset = Phase.objects.all()
    serializer_class = PhaseSerializer
    permission_classes = [AllowAny]