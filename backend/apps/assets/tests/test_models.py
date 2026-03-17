from django.test import TestCase
from apps.assets.models import Asset
from apps.projects.models import Project
from apps.companies.models import Company
from apps.users.models import User


class AssetModelTest(TestCase):
    """Test cases para el modelo Asset."""

    def setUp(self):
        """Set up test data."""
        self.company = Company.objects.create(name="Empresa Test", nit="123456789")
        self.user = User.objects.create_user(
            username="testuser",
            email="test@test.com",
            password="testpass123",
            role="CONSULTANT"
        )
        self.project = Project.objects.create(
            name="Test Project",
            company=self.company,
            created_by=self.user
        )

    def test_create_asset(self):
        """Verify Asset creation."""
        asset = Asset.objects.create(
            project=self.project,
            name="Server A",
            asset_type="SERVER",
            description="Main application server"
        )
        self.assertEqual(asset.name, "Server A")
        self.assertEqual(asset.asset_type, "SERVER")

    def test_asset_defaults(self):
        """Verify Asset default values."""
        asset = Asset.objects.create(
            project=self.project,
            name="Test Asset",
            asset_type="OTHER"
        )
        self.assertIsNotNone(asset.created_at)
