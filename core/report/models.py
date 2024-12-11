from django.db import models
from core.user.models import User
from core.gemini.models import GeminiAI

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(max_length=4000, null=True, blank=True)
    teacher = models.CharField(max_length=4000, null=True, blank=True)
    gemini_ai = models.ForeignKey(GeminiAI, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f"{self.content} {self.teacher}"
    
    