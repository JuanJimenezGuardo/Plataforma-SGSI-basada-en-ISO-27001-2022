from rest_framework.test import APITestCase
from rest_framework import status
from apps.companies.models import Company
from apps.contacts.models import Contact


class ContactAPITest(APITestCase):
    """Test cases para los endpoints de Contact."""

    def setUp(self):
        """Configurar datos de prueba."""
        self.company = Company.objects.create(name="Empresa Test", nit="123456789")
        self.contact_data = {
            "company": self.company.id,
            "full_name": "Carlos Mendez",
            "email": "carlos@test.com",
            "phone": "3009876543",
            "position": "Gerente TI",
            "is_active": True,
            "work_notes": "Contacto para proyectos de seguridad"
        }

    def test_create_contact_via_api(self):
        """Verificar creación de Contact por API."""
        response = self.client.post('/api/contacts/', self.contact_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_name'], "Carlos Mendez")
        self.assertEqual(response.data['work_notes'], "Contacto para proyectos de seguridad")

    def test_list_contacts_api(self):
        """Verificar listado de Contacts por API."""
        Contact.objects.create(company=self.company, full_name="Test 1", email="test1@test.com")
        Contact.objects.create(company=self.company, full_name="Test 2", email="test2@test.com")
        
        response = self.client.get('/api/contacts/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_contact_api(self):
        """Verificar obtención de un Contact por API."""
        contact = Contact.objects.create(
            company=self.company,
            full_name="Retrieve Test",
            email="retrieve@test.com",
            work_notes="Nota de prueba"
        )
        
        response = self.client.get(f'/api/contacts/{contact.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], "Retrieve Test")
        self.assertEqual(response.data['work_notes'], "Nota de prueba")

    def test_update_contact_work_notes_api(self):
        """Verificar actualización de work_notes por API."""
        contact = Contact.objects.create(
            company=self.company,
            full_name="Update Test",
            email="update@test.com",
            work_notes="Nota inicial"
        )
        
        update_data = {"work_notes": "Nota actualizada"}
        response = self.client.patch(f'/api/contacts/{contact.id}/', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['work_notes'], "Nota actualizada")

    def test_contact_field_visible_in_response(self):
        """Verificar que work_notes es visible en response."""
        contact = Contact.objects.create(
            company=self.company,
            full_name="Visibility Test",
            email="visibility@test.com",
            work_notes="Campo visible"
        )
        
        response = self.client.get(f'/api/contacts/{contact.id}/', format='json')
        self.assertIn('work_notes', response.data)
        self.assertEqual(response.data['work_notes'], "Campo visible")
