"""
Tests de autenticación JWT
Valida que el sistema de tokens funciona correctamente
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()


class JWTAuthenticationTest(TestCase):
    """Tests para autenticación con JWT"""
    
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
        self.refresh_url = '/api/token/refresh/'
    
    def test_login_successful(self):
        """Test: Login exitoso retorna access y refresh tokens"""
        response = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIsInstance(response.data['access'], str)
        self.assertIsInstance(response.data['refresh'], str)
    
    def test_login_invalid_credentials(self):
        """Test: Login con credenciales inválidas retorna 401"""
        response = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_login_missing_credentials(self):
        """Test: Login sin credenciales retorna 400"""
        response = self.client.post(self.token_url, {})
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_refresh_token_successful(self):
        """Test: Refresh token válido retorna nuevo access token"""
        # Primero obtener tokens
        login_response = self.client.post(self.token_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        refresh_token = login_response.data['refresh']
        
        # Luego refrescar
        response = self.client.post(self.refresh_url, {
            'refresh': refresh_token
        })
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
    
    def test_refresh_token_invalid(self):
        """Test: Refresh token inválido retorna 401"""
        response = self.client.post(self.refresh_url, {
            'refresh': 'invalid_token_string'
        })
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
