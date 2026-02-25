"""
Tests de endpoints protegidos con JWT
Valida que todos los endpoints requieren autenticación
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()


class ProtectedEndpointsTest(TestCase):
    """Tests para validar que los endpoints están protegidos"""
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@vit.local',
            password='testpass123',
            role='ADMIN'
        )
        
        # Obtener token válido
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.access_token = response.data['access']
        
        # Endpoints a probar
        self.protected_endpoints = [
            '/api/users/',
            '/api/companies/',
            '/api/projects/',
            '/api/phases/',
            '/api/tasks/',
        ]
    
    def test_endpoints_without_token_return_401(self):
        """Test: Endpoints sin token retornan 401"""
        for endpoint in self.protected_endpoints:
            response = self.client.get(endpoint)
            self.assertEqual(
                response.status_code,
                status.HTTP_401_UNAUTHORIZED,
                f"Endpoint {endpoint} debería retornar 401 sin token"
            )
    
    def test_endpoints_with_valid_token_return_200(self):
        """Test: Endpoints con token válido retornan 200"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        
        for endpoint in self.protected_endpoints:
            response = self.client.get(endpoint)
            self.assertEqual(
                response.status_code,
                status.HTTP_200_OK,
                f"Endpoint {endpoint} debería retornar 200 con token válido"
            )
    
    def test_endpoints_with_invalid_token_return_401(self):
        """Test: Endpoints con token inválido retornan 401"""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer invalid_token_123')
        
        for endpoint in self.protected_endpoints:
            response = self.client.get(endpoint)
            self.assertEqual(
                response.status_code,
                status.HTTP_401_UNAUTHORIZED,
                f"Endpoint {endpoint} debería retornar 401 con token inválido"
            )
    
    def test_token_endpoint_is_public(self):
        """Test: Endpoint de login no requiere autenticación"""
        response = self.client.post('/api/token/', {
            'username': 'testuser',
            'password': 'testpass123'
        })
        
        # Debe ser accesible sin token
        self.assertEqual(response.status_code, status.HTTP_200_OK)
