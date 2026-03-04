from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdmin

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestión de usuarios.
    Solo Admin puede crear/editar/eliminar usuarios.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    
    @action(detail=True, methods=['get'])
    def projects(self, request, pk=None):
        """
        Endpoint: GET /api/users/{id}/projects/
        Retorna lista de proyectos asignados al usuario.
        """
        from apps.projects.models import ProjectUser
        from apps.projects.serializers import ProjectSerializer
        
        user = self.get_object()
        projects = user.project_assignments.select_related('project').all()
        project_list = [pu.project for pu in projects]
        serializer = ProjectSerializer(project_list, many=True)
        return Response(serializer.data)
