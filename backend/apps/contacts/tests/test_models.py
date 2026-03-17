from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.companies.models import Company
from apps.contacts.models import Contact


class ContactModelTest(TestCase):
    """Test cases para el modelo Contact."""

    def setUp(self):
        """Configurar datos de prueba."""
        self.company = Company.objects.create(name="Empresa Test", nit="123456789")

    def test_create_contact_basic(self):
        """Verificar creación básica de Contact."""
        contact = Contact.objects.create(
            company=self.company,
            full_name="Juan Pérez",
            email="juan@test.com",
            phone="3001234567",
            position="Analista"
        )
        self.assertEqual(contact.full_name, "Juan Pérez")
        self.assertEqual(contact.email, "juan@test.com")
        self.assertTrue(contact.is_active)

    def test_create_contact_with_work_notes(self):
        """Verificar que work_notes se guarda correctamente."""
        contact = Contact.objects.create(
            company=self.company,
            full_name="María García",
            email="maria@test.com",
            work_notes="Contacto principal del departamento de seguridad"
        )
        self.assertEqual(contact.work_notes, "Contacto principal del departamento de seguridad")

    def test_unique_constraint_company_email(self):
        """Verificar restricción única de (company, email)."""
        Contact.objects.create(
            company=self.company,
            full_name="Pedro López",
            email="pedro@test.com"
        )
        
        # Intentar crear otro con el mismo email en la misma empresa
        duplicate = Contact(
            company=self.company,
            full_name="Otro Pedro",
            email="pedro@test.com"
        )
        
        with self.assertRaises(Exception):  # Puede ser IntegrityError
            duplicate.save()

    def test_contact_str_representation(self):
        """Verificar representación en string del Contact."""
        contact = Contact.objects.create(
            company=self.company,
            full_name="Ana Silva",
            email="ana@test.com"
        )
        expected = f"Ana Silva ({self.company.name})"
        self.assertEqual(str(contact), expected)

    def test_contact_defaults(self):
        """Verificar valores por defecto."""
        contact = Contact.objects.create(
            company=self.company,
            full_name="Test User",
            email="test@test.com"
        )
        self.assertTrue(contact.is_active)
        self.assertEqual(contact.work_notes, "")
        self.assertIsNotNone(contact.created_at)
        self.assertIsNotNone(contact.updated_at)
