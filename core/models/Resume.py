from django.db import models
from .Candidate import Candidate

class Resume(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.candidate.full_name
