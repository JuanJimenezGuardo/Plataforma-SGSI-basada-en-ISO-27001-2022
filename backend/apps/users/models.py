from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Modelo de Usuario personalizado que extiende AbstractUser.
    ✅ HEREDA: username, email, password, first_name, last_name, is_active, etc.
    ✅ AGREGA: role, phone con lógica específica para VIT
    """
    ROLE_CHOICES = (
        ('ADMIN', 'Administrador VIT'),
        ('CONSULTANT', 'Consultor'),
        ('CLIENT', 'Cliente'),
    )
    
    # Campos personalizados para VIT
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='CLIENT')
    phone = models.CharField(max_length=20, blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'users_user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return f'{self.get_full_name()} ({self.get_role_display()})'
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip() or self.username


class AuditLog(models.Model):
    """
    Registro de auditoría para trazabilidad de cambios
    Rastrea qué usuario hizo qué cambio en qué modelo y cuándo
    """
    ACTION_CHOICES = [
        ('CREATE', 'Creado'),
        ('UPDATE', 'Actualizado'),
        ('DELETE', 'Eliminado'),
    ]
    
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    entity_type = models.CharField(max_length=100)  # p.ej. 'Project', 'User', 'ProjectUser'
    entity_id = models.IntegerField()  # ID de la entidad que fue modificada
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_logs')
    changes = models.JSONField(blank=True, null=True)  # Cambios realizados (JSON)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users_auditlog'
        verbose_name = 'Registro de Auditoría'
        verbose_name_plural = 'Registros de Auditoría'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['entity_type', '-timestamp']),
            models.Index(fields=['user', '-timestamp']),
        ]
    
    def __str__(self):
        return f'{self.action} {self.entity_type} #{self.entity_id} by {self.user} at {self.timestamp}'