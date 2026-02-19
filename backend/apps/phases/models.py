from django.db import models
from apps.projects.models import Project

class Phase(models.Model):
    # Opciones para el estado de la fase
    PHASE_TYPE = (
        ('ASSESSMENT', 'Evaluación'),
        ('PLANNING', 'Planificación'),
        ('IMPLEMENTATION', 'Implementación'),
        ('AUDIT', 'Auditoría'),
        ('CERTIFICATION', 'Certificación'),
    )
    
    # Campos del modelo Phase
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='phases', verbose_name='Proyecto')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=PHASE_TYPE)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    order = models.IntegerField(default=0)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name} - {self.get_type_display()}'

    class Meta:
        db_table = 'phases_phase'
        verbose_name = 'Phase'
        verbose_name_plural = 'Phases'