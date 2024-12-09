from rest_framework.viewsets import ModelViewSet
from core.report.models import Report
from core.report.serializer import ReportSerializer
from django.contrib.admin import action
from rest_framework.permissions import IsAuthenticated
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from utils.generate_report import generate_pdf


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer