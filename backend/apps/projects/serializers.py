from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    # phases = PhaseSerializer(many=True, read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)
    created_by_name = serializers.CharField(source='created_by.get_full_name', read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'company', 'company_name', 'status', 'start_date', 'end_date', 'created_by', 'created_by_name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

