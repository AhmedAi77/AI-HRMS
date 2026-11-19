from rest_framework import serializers
from ..models import Resume
from django.core.validators import FileExtensionValidator


class ResumeSerializer(serializers.ModelSerializer):

    file = serializers.FileField(

        validators=[

            FileExtensionValidator(
                allowed_extensions=["pdf", "docx", "txt"]
            )
        ]
    )

    class Meta:
        model = Resume
        fields = "__all__"