from django.db import models
from core.user.models import UserQuestion

class GeminiAI(models.Model):
    user_question = models.ForeignKey(UserQuestion, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    text_body = models.CharField(max_length=4000, null=True,blank=True)
    
    def __str__(self):
        return f"{self.title} - {self.text_body}"
