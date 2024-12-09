from django.db import models
from core.user.models import User

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=4000)
    teacher = models.CharField(max_length=4000)
    
    def __str__(self):
        return f"{self.content} {self.teacher}"
    
    