from rest_framework.serializers import ModelSerializer
from core.user.models import User, UserQuestion

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class UserQuestionSerializer(ModelSerializer):
    class Meta:
        model = UserQuestion
        fields = "__all__"