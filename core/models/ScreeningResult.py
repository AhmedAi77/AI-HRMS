from django.db import models
from .Candidate import Candidate
from .JobPosition import JobPosition
from django.core.validators import MinValueValidator, MaxValueValidator

class ScreeningResult(models.Model):
    job_position = models.ForeignKey(JobPosition, on_delete=models.PROTECT)
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)

    score = models.FloatField(
        default=0.0,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(100.0)
        ]
    )

    missing_skills = models.JSONField(default=list,blank=True)

    summary = models.TextField()

    raw_report = models.TextField()

    generated_at = models.DateTimeField(auto_now_add=True)
    RECOMMENDATION_CHOICES = [
        ("proceed", "Proceed"),
        ("hold", "Hold"),
        ("reject", "Reject"),
    ]

    recommendation = models.CharField(
        max_length=10,
        choices=RECOMMENDATION_CHOICES
    )

    strengths = models.JSONField(default=list,blank=True)

    class Meta:
        ordering = ["-generated_at"]


    def __str__(self):
        return f"{self.candidate.full_name} - {self.job_position.title}"
