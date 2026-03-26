from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import User, AuditLog


@receiver(post_save, sender=User)
def log_user_save(sender, instance, created, **kwargs):
    """
    Signal para registrar creacion y actualizacion de usuarios en AuditLog.
    Nota: El usuario que realiza la accion puede ser diferente al usuario creado.
    """
    # En creacion/actualizacion de usuarios, no siempre tenemos el user que hace la accion
    # Por ahora registramos sin usuario (sistema) o el mismo usuario en caso de actualizacion
    action = 'CREATE' if created else 'UPDATE'
    user = None if created else instance
    
    changes = {
        'username': instance.username,
        'email': instance.email,
        'role': instance.role,
        'is_active': instance.is_active,
    }
    
    AuditLog.objects.create(
        user=user,
        action=action,
        entity_type='User',
        entity_id=instance.id,
        changes=changes
    )


@receiver(post_delete, sender=User)
def log_user_delete(sender, instance, **kwargs):
    """
    Signal para registrar eliminacion de usuarios en AuditLog.
    """
    AuditLog.objects.create(
        user=None,  # No podemos usar el usuario eliminado
        action='DELETE',
        entity_type='User',
        entity_id=instance.id,
        changes={'username': instance.username, 'email': instance.email, 'role': instance.role}
    )
