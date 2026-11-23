import re
from rest_framework import  serializers
from ..models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"

    def validate_phone(self, data):
        phone_regex = r"^\+?\d{9,15}$"

        if not re.fullmatch(phone_regex, data):
            raise serializers.ValidationError(
                "Enter a valid phone number."
            )

        return data