from django.contrib import admin
from.models import Department
from .models import JobPosition
from .models import Candidate
from.models import Resume
from .models import ScreeningResult
from .models import InterviewQuestionSet

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
    list_filter = ("created_at",)


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ("id", "title","department", "created_at")
    search_fields = ("title",)
    list_filter = ("created_at","department")


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone", "created_at",)
    search_fields = ("full_name","phone")
    list_filter = ("created_at",)


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "file", "uploaded_at",)
    search_fields = ("candidate__full_name", "file")
    list_filter = ("uploaded_at",)


@admin.register(ScreeningResult)
class ScreeningResultAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "recommendation", "score","job_position")
    search_fields = ("candidate__full_name", "job_position__title")
    list_filter = ("candidate__full_name", "recommendation")


@admin.register(InterviewQuestionSet)
class InterviewQuestionSetAdmin(admin.ModelAdmin):
    list_display = ("id", "candidate", "job_position", "screening_result","generated_at")
    search_fields = ("candidate__full_name", "job_position__title")
    list_filter = ("job_position","generated_at")