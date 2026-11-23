from django.urls import path
from .views.DepartmentView import create_department
from .views.JobPositionView import job_position_view
from .views.CandidateView import create_candidate
from .views.ResumeView import upload_resume
from .views.ScreeningResultView import get_screening_result
from .views.InterviewQuestionSetView import get_interview_question_sets


urlpatterns = [
    path("departments/", create_department, name="create_department"),

    path("job-positions/", job_position_view, name="create_job"),

    path("candidates/", create_candidate, name="create_candidate"),

    path("resumes/", upload_resume, name="create_resume"),

    path(
        "screening-results/<int:pk>/",
        get_screening_result,
        name="screening_result"
    ),

    path(
        "interview-questions/<int:pk>/",
        get_interview_question_sets,
        name="interview_questions"
    ),
]