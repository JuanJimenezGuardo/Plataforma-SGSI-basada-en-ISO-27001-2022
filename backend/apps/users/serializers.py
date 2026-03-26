from rest_framework import serializers
from .models import User, AuditLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'role', 'phone', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class AuditLogSerializer(serializers.ModelSerializer):
    """
    Serializer para AuditLog (solo lectura).
    Incluye información del usuario relacionado.
    """
    user_username = serializers.CharField(source='user.username', read_only=True)
    action_display = serializers.CharField(source='get_action_display', read_only=True)
    
    class Meta:
        model = AuditLog
        fields = [
            'id', 'user', 'user_username', 'action', 'action_display',
            'entity_type', 'entity_id', 'changes', 'timestamp'
        ]
        read_only_fields = ['id', 'timestamp']
        