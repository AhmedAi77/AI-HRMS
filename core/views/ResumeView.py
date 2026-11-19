from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.Serializer import ResumeSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class ResumeView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request):
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
