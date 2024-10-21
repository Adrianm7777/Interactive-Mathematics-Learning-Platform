from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnswerViewSet,ProblemViewSet,ProgressViewSet

router = DefaultRouter()
router.register(r'problems', ProblemViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'progress', ProgressViewSet)


urlpatterns = [
    path('', include(router.urls))
]