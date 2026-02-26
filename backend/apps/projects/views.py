from rest_framework import viewsets
from .models import Project, ProjectUser
from .serializers import ProjectSerializer, ProjectUserSerializer
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


class ProjectUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para asignación de usuarios a proyectos.
    Consultores y Admin pueden asignar usuarios a proyectos.
    Todos los autenticados pueden ver asignaciones.
    """
    queryset = ProjectUser.objects.select_related('project', 'user')
    serializer_class = ProjectUserSerializer
    permission_classes = [IsConsultantOrReadOnly]