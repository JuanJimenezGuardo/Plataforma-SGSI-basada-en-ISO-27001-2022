from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Project #, Phase, Task
from .serializers import ProjectSerializer #, PhaseSerializer, TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]