from django.urls import path
from .views import DepartmentView
from.views import JobPositionView
from.views import CandidateView
from .views import ResumeView
from .views import ScreeningResultView
from .views import InterviewQuestionSetView


urlpatterns = [
    path("departments/", DepartmentView.as_view(), name="create_department"),
    path("job-positions/", JobPositionView.as_view(), name="create_job"),
    path("candidates/", CandidateView.as_view(), name="create_candidate"),
    path("resumes/", ResumeView.as_view(), name="create_resume"),
    path(
        "screening-results/<int:pk>/",
        ScreeningResultView.as_view(),
        name="screening_result"
    ),
    path(
        "interview-questions/<int:pk>/",
         InterviewQuestionSetView.as_view(),
         name="interview_questions"
),

]