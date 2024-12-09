from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Report
from django.core.mail import EmailMultiAlternatives
from utils.generate_report import generate_pdf  

@receiver(post_save, sender=Report)
def generate_report_and_send_email(sender, instance, created, **kwargs):
    if created:  
        print('Estou sendo chamado')
        print(instance)
        response = instance.content
        print(response)
        print(instance.user)
        student = instance.user.email
        print(student)
        
        pdf: dict = generate_pdf(name_person=student, text=response, title=student, turma=student)
        print(pdf)
        try:
            subject = "Trabalho"
            recipient_list = [instance.teacher]  
            text_content = "arroz é bom"
            from_email = "martinsbarroskaua85@gmail.com"
            email = EmailMultiAlternatives(subject=subject, to=recipient_list, from_email=from_email, body=text_content)
            email.attach('trabalho', pdf.getvalue(), 'application/pdf')
            email.send()
        except Exception as error:
            print(f"Erro ao gerar ou enviar relatório: {error}")
