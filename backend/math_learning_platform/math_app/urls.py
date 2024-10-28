from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AnswerViewSet,ProblemViewSet

router = DefaultRouter()
router.register(r'problems', ProblemViewSet)
router.register(r'answers', AnswerViewSet)


urlpatterns = [
    path('', include(router.urls))
]