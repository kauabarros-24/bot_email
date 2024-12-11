from django.db.models.signals import post_save
from django.dispatch import receiver
from core.user.models import UserQuestion
import requests
import os

@receiver(post_save, sender=UserQuestion)
def InviteAI(created, instance, sender, **kwargs):
    if created:
        print('Estou sendo chamado')
        json = {
            "user_question": {
                "question": instance.question,
                "user": instance.user.id,
                "teacher_email": instance.teacher_mail
            }
        }
        requests.post(f"{os.getenv('REQUEST')}/gemini", json=json)
    
    