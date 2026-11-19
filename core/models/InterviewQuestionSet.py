from django.db import models
from .Candidate import  Candidate
from .JobPosition import JobPosition
from .ScreeningResult import  ScreeningResult


class InterviewQuestionSet(models.Model):

    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)

    job_position = models.ForeignKey(JobPosition, on_delete=models.PROTECT)

    screening_result = models.OneToOneField(
        ScreeningResult,
        on_delete=models.PROTECT
    )
    technical_questions = models.JSONField(default=list)

    behavioral_questions = models.JSONField(default=list)

    follow_up_questions = models.JSONField(default=list)

    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.candidate.full_name} - {self.job_position.title}"

