from rest_framework.viewsets import ModelViewSet
from core.user.models import UserQuestion
from core.gemini.models import GeminiAI
from core.gemini.serializer import GeminiAISerializer

class GeminiAIViewSet(ModelViewSet):
    queryset = GeminiAI.objects.all()
    serializer_class = GeminiAISerializer
    
    
    
    