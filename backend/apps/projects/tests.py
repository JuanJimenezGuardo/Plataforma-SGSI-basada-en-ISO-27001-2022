"""Tests for ProjectUser model and endpoints"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Project, ProjectUser
from apps.companies.models import Company
from datetime import date, timedelta

User = get_user_model()


class ProjectUserTestCase(TestCase):
    """Tests for ProjectUser model and API endpoints"""
    
    @classmethod
    def setUpTestData(cls):
        """Set up test data"""
        # Create a company
        cls.company = Company.objects.create(
            name="Test Company",
            rfc="RFC000001",
            email="company@test.com",
            phone="555-1234",
            address="Test Address",
            city="Test City",
            state="Test State",
            country="Colombia",
            contact_person="John Doe",
            contact_position="CEO"
        )
        
        # Create users with different roles
        cls.admin_user = User.objects.create_user(
            username="admin_user",
            email="admin@test.com",
            password="testpass123",
            role="ADMIN"
        )
        
        cls.consultant_user = User.objects.create_user(
            username="consultant_user",
            email="consultant@test.com",
            password="testpass123",
            role="CONSULTANT"
        )
        
        cls.client_user = User.objects.create_user(
            username="client_user",
            email="client@test.com",
            password="testpass123",
            role="CLIENT"
        )
        
        # Create a project
        cls.project = Project.objects.create(
            name="Test Project",
            description="Test project",
            company=cls.company,
            status="PLANNING",
            start_date=date.today(),
            end_date=date.today() + timedelta(days=365),
            created_by=cls.admin_user
        )
    
    def setUp(self):
        """Set up for each test"""
        self.client = APIClient()
        # Create tokens for test users
        refresh = RefreshToken.for_user(self.admin_user)
        self.admin_token = str(refresh.access_token)
        
        refresh = RefreshToken.for_user(self.consultant_user)
        self.consultant_token = str(refresh.access_token)
        
        refresh = RefreshToken.for_user(self.client_user)
        self.client_token = str(refresh.access_token)
    
    def test_create_project_user_as_consultant(self):
        """Consultant can create ProjectUser assignments"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.consultant_token}')
        
        data = {
            "project": self.project.id,
            "user": self.client_user.id,
            "role": "VIEWER"
        }
        
        response = self.client.post('/api/project-users/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['role'], "VIEWER")
        
        # Verify in database
        pu = ProjectUser.objects.get(project=self.project, user=self.client_user)
        self.assertEqual(pu.role, "VIEWER")
    
    def test_cannot_create_duplicate_project_user(self):
        """Cannot assign same user twice to same project"""
        # Create initial assignment
        ProjectUser.objects.create(
            project=self.project,
            user=self.client_user,
            role="CLIENT"
        )
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.consultant_token}')
        
        data = {
            "project": self.project.id,
            "user": self.client_user.id,
            "role": "CONSULTANT"
        }
        
        response = self.client.post('/api/project-users/', data, format='json')
        self.assertEqual(response.status_code, 400)
    
    def test_get_project_users_list(self):
        """Can retrieve list of ProjectUser assignments"""
        # Create some assignments
        ProjectUser.objects.create(
            project=self.project,
            user=self.admin_user,
            role="ADMIN"
        )
        ProjectUser.objects.create(
            project=self.project,
            user=self.consultant_user,
            role="CONSULTANT"
        )
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.admin_token}')
        response = self.client.get('/api/project-users/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
    
    def test_retrieve_specific_project_user(self):
        """Can retrieve specific ProjectUser assignment"""
        pu = ProjectUser.objects.create(
            project=self.project,
            user=self.consultant_user,
            role="CONSULTANT"
        )
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.admin_token}')
        response = self.client.get(f'/api/project-users/{pu.id}/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['role'], "CONSULTANT")
        self.assertEqual(response.data['username'], "consultant_user")
        self.assertEqual(response.data['project_name'], "Test Project")
    
    def test_update_project_user_role(self):
        """Can update ProjectUser role"""
        pu = ProjectUser.objects.create(
            project=self.project,
            user=self.client_user,
            role="VIEWER"
        )
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.consultant_token}')
        
        data = {"role": "CLIENT"}
        response = self.client.patch(f'/api/project-users/{pu.id}/', data, format='json')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['role'], "CLIENT")
        
        # Verify in database
        pu.refresh_from_db()
        self.assertEqual(pu.role, "CLIENT")
    
    def test_delete_project_user(self):
        """Consultant can delete ProjectUser assignments"""
        pu = ProjectUser.objects.create(
            project=self.project,
            user=self.client_user,
            role="VIEWER"
        )
        
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.consultant_token}')
        response = self.client.delete(f'/api/project-users/{pu.id}/')
        
        self.assertEqual(response.status_code, 204)
        self.assertFalse(ProjectUser.objects.filter(id=pu.id).exists())
    
    def test_client_cannot_create_project_user(self):
        """Client role cannot create ProjectUser assignments"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.client_token}')
        
        data = {
            "project": self.project.id,
            "user": self.consultant_user.id,
            "role": "CONSULTANT"
        }
        
        response = self.client.post('/api/project-users/', data, format='json')
        self.assertEqual(response.status_code, 403)
    
    def test_anonymous_cannot_access_project_users(self):
        """Anonymous user cannot access ProjectUser endpoint"""
        response = self.client.get('/api/project-users/')
        self.assertEqual(response.status_code, 401)
    
    def test_project_user_string_representation(self):
        """ProjectUser __str__ method works correctly"""
        pu = ProjectUser.objects.create(
            project=self.project,
            user=self.consultant_user,
            role="CONSULTANT"
        )
        
        expected_str = f"{self.consultant_user.username} - {self.project.name} (Consultor)"
        self.assertEqual(str(pu), expected_str)


class ProjectFilteringTestCase(TestCase):
    """Tests for Día 6: Project filtering by role and ProjectUser assignments"""
    
    @classmethod
    def setUpTestData(cls):
        """Set up test data for filtering tests"""
        # Create company
        cls.company = Company.objects.create(
            name="Filter Test Company",
            rfc="RFC999999",
            email="filter@test.com",
            phone="555-9999",
            address="Filter Address",
            city="Filter City",
            state="Filter State",
            country="Colombia",
            contact_person="Filter Person",
            contact_position="Manager"
        )
        
        # Create users
        cls.admin_user = User.objects.create_user(
            username="filter_admin",
            email="admin@filter.com",
            password="testpass123",
            role="ADMIN"
        )
        
        cls.consultant_user = User.objects.create_user(
            username="filter_consultant",
            email="consultant@filter.com",
            password="testpass123",
            role="CONSULTANT"
        )
        
        cls.client_user = User.objects.create_user(
            username="filter_client",
            email="client@filter.com",
            password="testpass123",
            role="CLIENT"
        )
        
        # Create 2 projects
        cls.project1 = Project.objects.create(
            name="Project 1",
            description="First project",
            company=cls.company,
            status="PLANNING",
            start_date=date.today(),
            created_by=cls.admin_user
        )
        
        cls.project2 = Project.objects.create(
            name="Project 2",
            description="Second project",
            company=cls.company,
            status="IN_PROGRESS",
            start_date=date.today(),
            created_by=cls.admin_user
        )
        
        # Assign client_user only to project1
        ProjectUser.objects.create(
            project=cls.project1,
            user=cls.client_user,
            role="CLIENT"
        )
        
        # Assign consultant_user to both projects
        ProjectUser.objects.create(
            project=cls.project1,
            user=cls.consultant_user,
            role="CONSULTANT"
        )
        ProjectUser.objects.create(
            project=cls.project2,
            user=cls.consultant_user,
            role="CONSULTANT"
        )
    
    def setUp(self):
        """Set up for each test"""
        self.client = APIClient()
        
        # Create tokens
        refresh = RefreshToken.for_user(self.admin_user)
        self.admin_token = str(refresh.access_token)
        
        refresh = RefreshToken.for_user(self.consultant_user)
        self.consultant_token = str(refresh.access_token)
        
        refresh = RefreshToken.for_user(self.client_user)
        self.client_token = str(refresh.access_token)
    
    def test_admin_sees_all_projects(self):
        """Admin role can see all projects"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.admin_token}')
        response = self.client.get('/api/projects/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
    
    def test_client_sees_only_assigned_projects(self):
        """Client role only sees projects where assigned via ProjectUser"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.client_token}')
        response = self.client.get('/api/projects/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Project 1")
    
    def test_consultant_sees_assigned_projects(self):
        """Consultant sees projects where assigned via ProjectUser"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.consultant_token}')
        response = self.client.get('/api/projects/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
    
    def test_project_users_endpoint(self):
        """GET /api/projects/{id}/users/ returns assigned users"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.admin_token}')
        response = self.client.get(f'/api/projects/{self.project1.id}/users/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)  # consultant and client
        
        usernames = [item['username'] for item in response.data]
        self.assertIn('filter_client', usernames)
        self.assertIn('filter_consultant', usernames)
    
    def test_user_projects_endpoint(self):
        """GET /api/users/{id}/projects/ returns user's assigned projects"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.admin_token}')
        response = self.client.get(f'/api/users/{self.client_user.id}/projects/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Project 1")
    
    def test_consultant_multiple_projects_endpoint(self):
        """GET /api/users/{id}/projects/ for consultant with multiple projects"""
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.admin_token}')
        response = self.client.get(f'/api/users/{self.consultant_user.id}/projects/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
