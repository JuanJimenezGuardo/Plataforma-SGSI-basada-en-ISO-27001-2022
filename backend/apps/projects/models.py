from django.db import models
from apps.companies.models import Company
from apps.users.models import User

# Choices para Project
PROJECT_STATUS_CHOICES = (
    ('PLANNING', 'Planeación'),
    ('IN_PROGRESS', 'En progreso'),
    ('COMPLETED', 'Completado'),
    ('ON_HOLD', 'En pausa'),
)

# Modelo Project
class Project(models.Model):
    """Proyecto ISO 27001 para una empresa"""
    name = models.CharField(max_length=255, verbose_name='Nombre del proyecto')
    description = models.TextField(blank=True, verbose_name='Descripción')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='projects', verbose_name='Empresa')
    status = models.CharField(max_length=20, choices=PROJECT_STATUS_CHOICES, default='PLANNING', verbose_name='Estado')
    start_date = models.DateField(verbose_name='Fecha de inicio')
    end_date = models.DateField(null=True, blank=True, verbose_name='Fecha de finalización')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='projects_created', verbose_name='Creado por')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')
    
    def __str__(self):
        return f'{self.name} - {self.company.name}'

    class Meta:
        db_table = 'projects_project'
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created_at']