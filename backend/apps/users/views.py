from rest_framework import viewsets
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
