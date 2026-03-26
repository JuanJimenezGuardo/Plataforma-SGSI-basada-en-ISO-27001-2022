from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AuditLogViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'audit-logs', AuditLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
