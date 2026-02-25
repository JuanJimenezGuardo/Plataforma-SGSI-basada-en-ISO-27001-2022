from rest_framework import viewsets
from .models import Project #, Phase, Task
from .serializers import ProjectSerializer #, PhaseSerializer, TaskSerializer
from apps.users.permissions import IsConsultantOrReadOnly

class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestión de proyectos.
    Consultores y Admin pueden crear/editar proyectos.
    Todos los autenticados pueden ver proyectos.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsConsultantOrReadOnly]