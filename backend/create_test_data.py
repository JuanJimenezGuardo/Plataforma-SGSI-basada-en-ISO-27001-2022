#!/usr/bin/env python
"""Create test data for ProjectUser endpoint"""

import os
import django
from datetime import date, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')
django.setup()

from django.contrib.auth import get_user_model
from apps.companies.models import Company
from apps.projects.models import Project, ProjectUser

User = get_user_model()

print("=" * 60)
print("Creating test data...")
print("=" * 60)

# Create a company
print("\n1. Creating Company...")
company, created = Company.objects.get_or_create(
    name="VIT Solutions",
    rfc="RFC000001",
    defaults={
        "email": "info@vit.com",
        "phone": "555-1234",
        "address": "Calle Principal 123",
        "city": "Medellín",
        "state": "Antioquia",
        "country": "Colombia",
        "contact_person": "John Doe",
        "contact_position": "CEO"
    }
)
if created:
    print(f"✓ Created company: {company.name}")
else:
    print(f"✓ Company already exists: {company.name}")

# Create a project
print("\n2. Creating Project...")
admin_user = User.objects.get(username='admin')
start_date = date.today()
end_date = start_date + timedelta(days=365)

project, created = Project.objects.get_or_create(
    name="ISO 27001 Implementation",
    company=company,
    defaults={
        "description": "Implementing ISO 27001 SGSI",
        "status": "PLANNING",
        "start_date": start_date,
        "end_date": end_date,
        "created_by": admin_user
    }
)
if created:
    print(f"✓ Created project: {project.name}")
else:
    print(f"✓ Project already exists: {project.name}")

# Create a consultant user
print("\n3. Creating users...")
consultant, created = User.objects.get_or_create(
    username='consultant1',
    defaults={
        "email": "consultant@example.com",
        "first_name": "Carlos",
        "last_name": "Consultor",
        "role": "CONSULTANT",
    }
)
if created:
    consultant.set_password("pass123")
    consultant.save()
    print(f"✓ Created consultant: {consultant.username}")
else:
    print(f"✓ Consultant already exists: {consultant.username}")

# Create a client user
client, created = User.objects.get_or_create(
    username='client1',
    defaults={
        "email": "client@example.com",
        "first_name": "Juan",
        "last_name": "Cliente",
        "role": "CLIENT",
    }
)
if created:
    client.set_password("pass123")
    client.save()
    print(f"✓ Created client: {client.username}")
else:
    print(f"✓ Client already exists: {client.username}")

# Create ProjectUser assignments
print("\n4. Creating ProjectUser assignments...")

# Admin as project admin
pu1, created = ProjectUser.objects.get_or_create(
    project=project,
    user=admin_user,
    defaults={"role": "ADMIN"}
)
if created:
    print(f"✓ Assigned {admin_user.username} as ADMIN to project")
else:
    print(f"✓ Assignment already exists: {admin_user.username}")

# Consultant as project consultant
pu2, created = ProjectUser.objects.get_or_create(
    project=project,
    user=consultant,
    defaults={"role": "CONSULTANT"}
)
if created:
    print(f"✓ Assigned {consultant.username} as CONSULTANT to project")
else:
    print(f"✓ Assignment already exists: {consultant.username}")

# Client as project client
pu3, created = ProjectUser.objects.get_or_create(
    project=project,
    user=client,
    defaults={"role": "CLIENT"}
)
if created:
    print(f"✓ Assigned {client.username} as CLIENT to project")
else:
    print(f"✓ Assignment already exists: {client.username}")

print("\n" + "=" * 60)
print("Test data created successfully!")
print("=" * 60)
print(f"\nSummary:")
print(f"  - Company: {company.name} (ID: {company.id})")
print(f"  - Project: {project.name} (ID: {project.id})")
print(f"  - ProjectUser assignments: {ProjectUser.objects.filter(project=project).count()}")
