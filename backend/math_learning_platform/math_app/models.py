from django.db import models

class Problem(models.Model):
    question = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=100)

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
    
