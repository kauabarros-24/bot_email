from core.gemini.models import GeminiAI
from rest_framework.serializers import ModelSerializer

class GeminiAISerializer(ModelSerializer):
    class Meta:
        model = GeminiAI
        fields = "__all__"