from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter
from core.user.views import UserViewSet, UserQuestionViewSet
from core.report.views import ReportViewSet
from core.gemini.views import GeminiAIViewSet

router = DefaultRouter()
router.register('gemini', GeminiAIViewSet, basename="gemini")
router.register('report', ReportViewSet, basename="report")
router.register('question', UserQuestionViewSet, basename="question")
router.register('user', UserViewSet, basename="user")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api/', include(router.urls)),
    
]
