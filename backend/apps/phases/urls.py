from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PhaseViewSet

router=DefaultRouter()
router.register(r'phases',PhaseViewSet)

urlpatterns=[
    path('',include(router.urls))
]
