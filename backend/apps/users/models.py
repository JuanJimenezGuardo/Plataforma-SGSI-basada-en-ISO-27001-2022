from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    """
    Modelo de Usuario personalizado que extiende AbstractUser.
    HEREDA: username, email, password, first_name, last_name, is_active, etc.
    AGREGA: role, phone con logica especifica para VIT
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
    Modelo para registrar cambios en entidades del sistema (trazabilidad).
    Registra quien hizo que, cuando y sobre que entidad.
    """
    ACTION_CHOICES = (
        ('CREATE', 'Creacion'),
        ('UPDATE', 'Actualizacion'),
        ('DELETE', 'Eliminacion'),
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='audit_logs',
        verbose_name='Usuario'
    )
    action = models.CharField(max_length=10, choices=ACTION_CHOICES, verbose_name='Accion')
    entity_type = models.CharField(max_length=50, verbose_name='Tipo de entidad')
    entity_id = models.IntegerField(verbose_name='ID de entidad')
    changes = models.JSONField(null=True, blank=True, verbose_name='Cambios realizados')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Fecha y hora')
    
    class Meta:
        db_table = 'audit_logs'
        verbose_name = 'Registro de auditoria'
        verbose_name_plural = 'Registros de auditoria'
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['entity_type', 'entity_id']),
            models.Index(fields=['user', 'timestamp']),
            models.Index(fields=['timestamp']),
        ]
    
    def __str__(self):
        user_str = self.user.username if self.user else 'Sistema'
        return f'{user_str} - {self.get_action_display()} {self.entity_type} #{self.entity_id} ({self.timestamp.strftime("%Y-%m-%d %H:%M")})'
