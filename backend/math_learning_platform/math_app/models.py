from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    question = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.question
    
class Answer(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.problem.question} - {self.user_answer}"
    
    def save(self, *args, **kwargs):
        self.is_correct = self.user_answer.strip() == self.problem.correct_answer.strip()
        super().save(*args, **kwargs)
    
class Progress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    completed_problem = models.IntegerField(default=0)
    correct_answers = models.IntegerField(default=0)
    current_difficulty = models.CharField(max_length=50, default='easy')

    def __str__(self):
        return f"{self.user.username}'s Progress"