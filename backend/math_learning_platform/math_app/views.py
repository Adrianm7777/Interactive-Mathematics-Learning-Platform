from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Answer, Problem
from .serializers import AnswerSerializer, ProblemSerializer
from rest_framework.decorators import action

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    
    def list(self, request, *args, **kwargs):
        problems = Problem.objects.all()
        serializer = self.get_serializer(problems, many=True)
        return Response(serializer.data)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    @action(detail=False, methods=['post'])
    def submit_answer(self, request):
        problem = get_object_or_404(Problem, id=request.data.get('problem'))
        user_answer = request.data.get('user_answer')

        is_correct = user_answer.strip() == problem.correct_answer.strip()

        return Response({"is_correct": is_correct})
