from rest_framework import serializers
from ..models import JobPosition


class JobPositionSerializer(serializers.ModelSerializer):

    department_name = serializers.CharField(
        source='department.name',
        read_only=True
    )

    class Meta:
        model = JobPosition
        fields = "__all__"

    def validate_required_skills(self, value):

        if not isinstance(value, list):
            raise serializers.ValidationError(
                "Required skills must be a list."
            )

        if not all(isinstance(skill, str) for skill in value):
            raise serializers.ValidationError(
                "Each skill must be a string."
            )

        return value