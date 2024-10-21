from django.shortcuts import render
from rest_framework import viewsets
from .models import Answer,Problem,Progress
from .serializers import AnswerSerializer,ProblemSerializer,ProgressSerializer

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class =AnswerSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer