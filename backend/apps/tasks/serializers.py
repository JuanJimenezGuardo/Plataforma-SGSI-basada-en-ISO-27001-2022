from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','name','description','phase','assigned_to','priority','status','due_date','completion_date','created_at','updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']