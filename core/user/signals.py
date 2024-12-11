from django.db.models.signals import post_save
from django.dispatch import receiver
from core.user.models import UserQuestion
import requests
import os

@receiver(post_save, sender=UserQuestion)
def invite_ai(sender, instance, created, **kwargs):
    if created:
        print("Sinal de criação acionado")
        api_url = os.getenv("REQUEST")
        if not api_url:
            print("Erro: Variável de ambiente 'REQUEST' não configurada")
            return
        
        json_data = {
            "user_question":instance.pk
        }
        
        try:
            response = requests.post(f"{api_url}/gemini/", json=json_data)
            response.raise_for_status()
            print("Resposta da API:", response.json())
        except requests.exceptions.RequestException as e:
            print("Erro ao fazer a requisição para a API:", e)
