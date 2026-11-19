from rest_framework import  serializers
from ..models import JobPosition

class JobPositionSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(
        source='department.name',
        read_only=True
    )
    class Meta:
        model = JobPosition
        fields  = "__all__"
