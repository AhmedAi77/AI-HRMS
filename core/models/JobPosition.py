from django.db import models
from .Department import Department

class JobPosition(models.Model):
    title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    description = models.TextField()
    required_skills = models.JSONField(default=list,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
