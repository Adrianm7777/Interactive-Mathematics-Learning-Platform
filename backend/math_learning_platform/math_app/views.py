from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Answer, Problem, Progress
from .serializers import AnswerSerializer, ProblemSerializer, ProgressSerializer

class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    
    def list(self, request, *args, **kwargs):
        user = request.user if request.user.is_authenticated else None
        difficulty = request.query_params.get('difficulty', 'easy')
        problems = Problem.objects.filter(difficulty=difficulty)
        serializer = self.get_serializer(problems, many=True)
        return Response(serializer.data)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    @action(detail=False, methods=['post'])
    def submit_answer(self, request):
        user = request.user
        progress = get_object_or_404(Progress, user=user)
        problem = get_object_or_404(Problem, id=request.data.get('problem'))
        user_answer = request.data.get('user_answer')

        is_correct = user_answer.strip() == problem.correct_answer.strip()

        if is_correct:
            progress.correct_answers += 1
        else:
            progress.correct_answers = max(progress.correct_answers - 1, 0)

        progress.completed_problem += 1
        progress.save()

        adjust_difficulty(progress)

        return Response({"is_correct": is_correct})

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer


def get_queryset(self):
        return Progress.objects.filter(user=self.request.user)

def adjust_difficulty(progress):
    if progress.correct_answers >= 10:
        progress.current_difficulty = 'hard'
    elif progress.correct_answers >= 5:
        progress.current_difficulty = 'medium'
    else:
        progress.current_difficulty = 'easy'
    
    progress.save()
