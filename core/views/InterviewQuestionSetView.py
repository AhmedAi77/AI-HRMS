from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.Serializer import InterviewQuestionSetSerializer
from core.models import InterviewQuestionSet


@api_view(['GET'])
def get_interview_question_sets(request,pk):
        try:
            result = InterviewQuestionSet.objects.get(pk=pk)
            serializer = InterviewQuestionSetSerializer(result)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except InterviewQuestionSet.DoesNotExist:
            return Response(
                {"error": "Interview question set not found"},
                status=status.HTTP_404_NOT_FOUND
            )




