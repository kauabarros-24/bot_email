from django.db.models.signals import post_save
from django.dispatch import receiver
from core.report.models import Report
from django.core.mail import EmailMultiAlternatives
from utils.generate_report import generate_pdf

@receiver(post_save, sender=Report)
def generate_report_and_send_email(sender, instance, created, **kwargs):
    if created:  
        student = instance.gemini_ai.user_question.user
        response = instance.gemini_ai.text_body
        title = instance.gemini_ai.title
        
        pdf: dict = generate_pdf(name_person=student.name, text=response, title=title, turma=None)
        print(pdf)
        try:
            subject = "O trabalho foi finalizado!"
            recipient_list = [instance.gemini_ai.user_question.teacher_mail]  
            text_content = "Prof, tudo bem? Ei, trabalho finalizado"
            from_email = student.email
            email = EmailMultiAlternatives(subject=subject, to=recipient_list, from_email=from_email, body=text_content)
            email.attach('trabalho', pdf.getvalue(), 'application/pdf')
            email.send()
        except Exception as error:
            print(f"Erro ao gerar ou enviar relatório: {error}")
