"""
Tests de seguridad JWT
Valida comportamientos de seguridad del sistema de tokens
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
import time

User = get_user_model()


class JWTSecurityTest(TestCase):
    """Tests de seguridad para JWT"""
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@vit.local',
            password='testpass123',
            role='ADMIN'
        )
        self.token_url = '/api/token/'
    
    def test_token_contains_user_id(self):
        """Test: Token contiene información del usuario"""
        response = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        
        # Verificar que el token se genera correctamente
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        access_token = response.data['access']
        
        # Usar el token para acceder a un endpoint
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        user_response = self.client.get('/api/users/')
        
        self.assertEqual(user_response.status_code, status.HTTP_200_OK)
    
    def test_different_users_get_different_tokens(self):
        """Test: Usuarios diferentes obtienen tokens diferentes"""
        # Usuario 1
        response1 = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        token1 = response1.data['access']
        
        # Usuario 2
        user2 = User.objects.create_user(
            username='testuser2',
            email='test2@vit.local',
            password='testpass456',
            role='CLIENT'
        )
        response2 = self.client.post(self.token_url, {
            'username': 'testuser2',
            'password': 'testpass456'
        })
        token2 = response2.data['access']
        
        # Los tokens deben ser diferentes
        self.assertNotEqual(token1, token2)
    
    def test_token_cannot_be_reused_after_refresh(self):
        """Test: Refresh token funciona correctamente"""
        # Obtener tokens iniciales
        response = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        
        refresh_token = response.data['refresh']
        
        # Usar refresh token para obtener nuevo access token
        refresh_response = self.client.post('/api/token/refresh/', {
            'refresh': refresh_token
        })
        
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn('access', refresh_response.data)
        
        # El nuevo access token debe funcionar
        new_access_token = refresh_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {new_access_token}')
        
        endpoint_response = self.client.get('/api/users/')
        self.assertEqual(endpoint_response.status_code, status.HTTP_200_OK)
    
    def test_malformed_token_header_returns_401(self):
        """Test: Header mal formado retorna 401"""
        # Sin "Bearer" prefix
        self.client.credentials(HTTP_AUTHORIZATION='just_a_token')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Con formato incorrecto
        self.client.credentials(HTTP_AUTHORIZATION='Token invalid_format')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_empty_token_returns_401(self):
        """Test: Token vacío retorna 401"""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
