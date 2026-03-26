"""
Permisos personalizados por rol para VIT
Define reglas de acceso basadas en el rol del usuario
"""
from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """
    Permiso para usuarios con rol ADMIN
    Uso: Solo administradores del sistema pueden acceder
    """
    message = "Solo los administradores pueden realizar esta acción."
    
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.role == 'ADMIN'
        )


class IsConsultant(permissions.BasePermission):
    """
    Permiso para usuarios con rol CONSULTANT o ADMIN
    Uso: Consultores pueden gestionar proyectos, diagnósticos, SoA
    """
    message = "Solo los consultores pueden realizar esta acción."
    
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.role in ['CONSULTANT', 'ADMIN']
        )


class IsClient(permissions.BasePermission):
    """
    Permiso para usuarios con rol CLIENT, CONSULTANT o ADMIN
    Uso: Clientes pueden ver sus propios proyectos y datos
    """
    message = "No tienes permisos para acceder a este recurso."
    
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.role in ['CLIENT', 'CONSULTANT', 'ADMIN']
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permiso que permite lectura a todos los autenticados,
    pero solo Admin puede modificar
    Uso: Listas de referencia, catálogos, configuración del sistema
    """
    message = "Solo los administradores pueden modificar este recurso."
    
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        # Lectura permitida para todos los autenticados
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Escritura solo para Admin
        return request.user.role == 'ADMIN'


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permiso a nivel de objeto: el dueño o Admin pueden modificar
    Uso: Proyectos, documentos, evidencias propias del usuario
    """
    message = "Solo el propietario o un administrador pueden modificar este recurso."
    
    def has_object_permission(self, request, view, obj):
        # Admin siempre tiene acceso
        if request.user.role == 'ADMIN':
            return True
        
        # Verificar si el objeto tiene un campo 'created_by' o 'user'
        if hasattr(obj, 'created_by'):
            return obj.created_by == request.user
        elif hasattr(obj, 'user'):
            return obj.user == request.user
        
        # Si no hay campo de owner, denegar acceso
        return False


class IsConsultantOrReadOnly(permissions.BasePermission):
    """
    Permiso que permite lectura a todos,
    pero solo Consultants y Admin pueden modificar
    Uso: Creación de proyectos, fases, tareas
    """
    message = "Solo los consultores pueden modificar este recurso."
    
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        # Lectura permitida para todos los autenticados
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Escritura solo para Consultant y Admin
        return request.user.role in ['CONSULTANT', 'ADMIN']
