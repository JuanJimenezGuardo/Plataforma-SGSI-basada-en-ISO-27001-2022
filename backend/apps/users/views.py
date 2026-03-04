from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import User, AuditLog
from .serializers import UserSerializer, AuditLogSerializer
from .permissions import IsAdmin

class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestion de usuarios.
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


class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet para registros de auditoria (solo lectura).
    Permite filtrar por user, entity_type y fecha (timestamp).
    """
    queryset = AuditLog.objects.select_related('user').all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user', 'entity_type', 'action']
    ordering_fields = ['timestamp', 'entity_type', 'action']
    ordering = ['-timestamp']
