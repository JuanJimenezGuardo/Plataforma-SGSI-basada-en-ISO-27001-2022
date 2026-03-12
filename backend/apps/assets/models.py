from django.db import models
from apps.projects.models import Project


class Asset(models.Model):

    ASSET_TYPES = [
        ("hardware", "Hardware"),
        ("software", "Software"),
        ("information", "Information"),
        ("service", "Service"),
    ]

    CLASSIFICATIONS = [
        ("public", "Public"),
        ("internal", "Internal"),
        ("confidential", "Confidential"),
        ("restricted", "Restricted"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="assets"
    )

    name = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=50, choices=ASSET_TYPES)
    owner = models.CharField(max_length=255)
    classification = models.CharField(max_length=50, choices=CLASSIFICATIONS)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name