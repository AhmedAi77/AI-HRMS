from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.Serializer import ScreeningResultSerializer
from core.models import ScreeningResult

class ScreeningResultView(APIView):
    def get (self, request,pk):
        try:
            result= ScreeningResult.objects.get(pk=pk)
            serializer = ScreeningResultSerializer(result)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except ScreeningResult.DoesNotExist:
            return Response(
                {"error": "No such ScreeningResult"},
                status=status.HTTP_404_NOT_FOUND
            )




