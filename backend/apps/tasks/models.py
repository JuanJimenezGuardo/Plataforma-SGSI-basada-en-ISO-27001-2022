from django.db import models
from apps.phases.models import Phase
from apps.users.models import User

PRIORITY_CHOICES = (
    ('LOW', 'Baja'),
    ('MEDIUM', 'Media'),
    ('HIGH', 'Alta'),
    ('CRITICAL', 'Crítica'),
)

STATUS_CHOICES = (
    ('PENDING', 'Pendiente'),
    ('IN_PROGRESS', 'En progreso'),
    ('COMPLETED', 'Completada'),
)

class Task(models.Model):
    phase = models.ForeignKey(Phase, on_delete=models.CASCADE, related_name='tasks', verbose_name='Fase')
    name = models.CharField(max_length=150, verbose_name='Nombre')
    description = models.TextField(blank=True, verbose_name='Descripción')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks_assigned', verbose_name='Asignado a')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM', verbose_name='Prioridad')
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING', verbose_name='Estado')
    due_date = models.DateField(null=True, blank=True, verbose_name='Fecha límite')
    completion_date = models.DateField(null=True, blank=True, verbose_name='Fecha de completado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')



    def __str__(self):
        return f'{self.name} - {self.phase.name}'
    
    class Meta:
        db_table = 'tasks_task'
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-created_at']