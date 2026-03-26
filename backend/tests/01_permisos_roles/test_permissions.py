"""Tests de permisos y smoke de endpoints para el checkpoint de sprint.

Estos tests estan pensados para ejecutarse con:
    python manage.py test tests_demo.test_permissions
"""

from datetime import date

from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.companies.models import Company
from apps.projects.models import Project, ProjectUser
from apps.users.models import User


class PermissionsCheckpointTests(TestCase):
    ENDPOINTS_REQUIRING_AUTH = [
        "/api/users/",
        "/api/companies/",
        "/api/projects/",
        "/api/audit-logs/",
    ]

    SMOKE_ENDPOINTS = [
        "/api/users/",
        "/api/companies/",
        "/api/projects/",
        "/api/project-users/",
        "/api/phases/",
        "/api/tasks/",
        "/api/audit-logs/",
    ]

    @classmethod
    def setUpTestData(cls):
        cls.admin_user = User.objects.create_user(
            username="test_admin",
            email="admin@test.com",
            password="test123",
            role="ADMIN",
        )
        cls.consultant_user = User.objects.create_user(
            username="test_consultant",
            email="consultant@test.com",
            password="test123",
            role="CONSULTANT",
        )
        cls.client_user = User.objects.create_user(
            username="test_client",
            email="client@test.com",
            password="test123",
            role="CLIENT",
        )

        cls.company = Company.objects.create(
            name="Test Company Permissions",
            rfc="TCP010101ABC",
            email="test@company.com",
            phone="555-9999",
            address="Test Address",
            city="Test City",
            state="Test State",
            country="Colombia",
        )

        cls.project = Project.objects.create(
            name="Test Project Permissions",
            company=cls.company,
            status="PLANNING",
            planned_start_date=date(2026, 3, 1),
            created_by=cls.admin_user,
        )

        ProjectUser.objects.create(
            user=cls.consultant_user,
            project=cls.project,
            role="CONSULTANT",
        )

    def _auth_header(self, user):
        token = str(RefreshToken.for_user(user).access_token)
        return {"HTTP_AUTHORIZATION": f"Bearer {token}"}

    def _response_results(self, response):
        data = response.json()
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            results = data.get("results")
            if isinstance(results, list):
                return results
            return []
        return []

    def test_endpoints_require_authentication(self):
        for endpoint in self.ENDPOINTS_REQUIRING_AUTH:
            with self.subTest(endpoint=endpoint):
                response = self.client.get(endpoint)
                self.assertEqual(response.status_code, 401)

    def test_users_endpoint_only_admin(self):
        response_admin = self.client.get("/api/users/", **self._auth_header(self.admin_user))
        response_consultant = self.client.get(
            "/api/users/", **self._auth_header(self.consultant_user)
        )
        response_client = self.client.get("/api/users/", **self._auth_header(self.client_user))

        self.assertEqual(response_admin.status_code, 200)
        self.assertEqual(response_consultant.status_code, 403)
        self.assertEqual(response_client.status_code, 403)

    def test_projects_visibility_by_role(self):
        response_admin = self.client.get("/api/projects/", **self._auth_header(self.admin_user))
        response_consultant = self.client.get(
            "/api/projects/", **self._auth_header(self.consultant_user)
        )
        response_client = self.client.get("/api/projects/", **self._auth_header(self.client_user))

        self.assertEqual(response_admin.status_code, 200)
        self.assertEqual(response_consultant.status_code, 200)
        self.assertEqual(response_client.status_code, 200)

        admin_projects = self._response_results(response_admin)
        consultant_projects = self._response_results(response_consultant)
        client_projects = self._response_results(response_client)

        self.assertGreaterEqual(len(admin_projects), 1)
        self.assertEqual(len(consultant_projects), 1)
        self.assertEqual(len(client_projects), 0)

    def test_audit_logs_read_only_for_all_roles(self):
        for user in (self.admin_user, self.consultant_user, self.client_user):
            with self.subTest(user=user.username):
                response = self.client.get("/api/audit-logs/", **self._auth_header(user))
                self.assertEqual(response.status_code, 200)

    def test_smoke_endpoints_do_not_return_500(self):
        for endpoint in self.SMOKE_ENDPOINTS:
            for user in (self.admin_user, self.consultant_user, self.client_user):
                with self.subTest(endpoint=endpoint, user=user.username):
                    response = self.client.get(endpoint, **self._auth_header(user))
                    self.assertLess(response.status_code, 500)
