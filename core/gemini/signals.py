from django.db.models.signals import post_save
from django.dispatch import receiver
from core.gemini.models import GeminiAI
import requests
from utils.ai_config import Gemini
import os

@receiver(post_save, sender=GeminiAI)
def request_ai(sender, created, instance, **kwargs):
    if created:
        print("Estou sendo chamado")
        instruction = instance.user_question.question
        
        gemini = Gemini()
        response = gemini.generateText(instruction=instruction)
        
        if not response:
            return "Without response"
        else:
            instance.title = response['title']
            instance.text_body = response['body']
            instance.save()        
            
            json_request = {
                "gemini_ai": instance.id
            }
            try:
                response = requests.post(f"{os.getenv('REQUEST')}/report", json=json_request)  # Corrigido os.getenv
                print(response)
            except Exception as e:
                print(e)
