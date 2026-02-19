from rest_framework import serializers
from .models import Phase

class PhaseSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Phase
        fields=['id','name','type','description','start_date','end_date','order','created_at','updated_at','project']
        read_only_fields = ['id', 'created_at', 'updated_at']


