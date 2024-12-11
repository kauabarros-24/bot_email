from django.db.models.signals import post_save
from django.dispatch import receiver
from core.gemini.models import GeminiAI
import requests
import os
from core.gemini.ai_config import generate_ai_content

@receiver(post_save, sender=GeminiAI)
def request_ai(sender, instance, created, **kwargs):
    if created:
        print("Arroz")
        question = instance.user_question.question
        result = generate_ai_content(instruction=question)
        
        instance.title = result['title']
        instance.text_body = result['original_text']
        instance.save()

        request_json = {
            "gemini_ai": {
                "title": instance.title,
                "text_body": instance.text_body,
                "user_question": instance.user_question.question,  # Adicionar outros campos necessários
            }
        }

        try:
            response = requests.post(f"{os.getenv('REQUEST')}/report", json=request_json)
            
            if response.status_code == 201:
                print('Requisição bem-sucedida')
            else:
                print(f"Erro na requisição: {response.status_code} - {response.text}")

        except requests.RequestException as e:
            print(f"Erro ao fazer a requisição: {e}")
