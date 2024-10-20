from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    question = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.question
    
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.problem.question}"
    
class Progress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    completed_problem = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s Progress"