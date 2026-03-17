from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date
from apps.companies.models import Company
from apps.projects.models import Project
from apps.documents.models import Document
from apps.users.models import User


class DocumentAPITest(APITestCase):
    """Test cases para los endpoints de Document."""

    def setUp(self):
        """Configurar datos de prueba."""
        self.company = Company.objects.create(name="Empresa Test", nit="123456789")
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="testpass123",
            role="CONSULTANT"
        )
        self.project = Project.objects.create(
            name="Proyecto Test",
            company=self.company,
            created_by=self.user
        )
        self.document_data = {
            "project": self.project.id,
            "title": "Documento de Prueba",
            "doc_type": "POLICY",
            "status": "DRAFT",
            "version": "1.0",
            "planned_date": "2026-03-20",
            "actual_date": "2026-03-22"
        }

    def test_list_documents_api(self):
        """Verificar listado de Documents por API."""
        Document.objects.create(
            project=self.project,
            title="Doc 1",
            doc_type="POLICY",
            status="DRAFT"
        )
        Document.objects.create(
            project=self.project,
            title="Doc 2",
            doc_type="PROCEDURE",
            status="DRAFT"
        )
        
        response = self.client.get('/api/documents/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_document_api(self):
        """Verificar obtención de un Document por API."""
        doc = Document.objects.create(
            project=self.project,
            title="Retrieve Test",
            doc_type="REPORT",
            status="DRAFT",
            planned_date=date(2026, 3, 20),
            actual_date=date(2026, 3, 22)
        )
        
        response = self.client.get(f'/api/documents/{doc.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Retrieve Test")
        self.assertEqual(response.data['planned_date'], "2026-03-20")
        self.assertEqual(response.data['actual_date'], "2026-03-22")

    def test_update_document_dates_api(self):
        """Verificar actualización de planned_date y actual_date por API."""
        doc = Document.objects.create(
            project=self.project,
            title="Update Test",
            doc_type="POLICY",
            status="DRAFT",
            planned_date=date(2026, 3, 20)
        )
        
        update_data = {
            "planned_date": "2026-03-25",
            "actual_date": "2026-03-26"
        }
        response = self.client.patch(f'/api/documents/{doc.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['planned_date'], "2026-03-25")
        self.assertEqual(response.data['actual_date'], "2026-03-26")

    def test_document_fields_visible_in_response(self):
        """Verificar que planned_date y actual_date son visibles en response."""
        doc = Document.objects.create(
            project=self.project,
            title="Visibility Test",
            doc_type="POLICY",
            status="DRAFT",
            planned_date=date(2026, 3, 20),
            actual_date=date(2026, 3, 22)
        )
        
        response = self.client.get(f'/api/documents/{doc.id}/', format='json')
        self.assertIn('planned_date', response.data)
        self.assertIn('actual_date', response.data)
        self.assertEqual(response.data['planned_date'], "2026-03-20")
        self.assertEqual(response.data['actual_date'], "2026-03-22")

    def test_create_document_with_dates(self):
        """Verificar creación de Document con fechas por API."""
        response = self.client.post('/api/documents/', self.document_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['planned_date'], "2026-03-20")
        self.assertEqual(response.data['actual_date'], "2026-03-22")
