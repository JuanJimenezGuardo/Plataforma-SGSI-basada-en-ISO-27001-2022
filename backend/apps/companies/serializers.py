from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'rfc', 'email', 'phone', 'address', 'city', 'state', 'country', 'contact_person', 'contact_position']
