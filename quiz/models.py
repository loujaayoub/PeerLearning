from django.db import models
from account.models import User,Skill
# Create your models here.
class Quiz(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    correctAnswerMark = models.IntegerField(default=1)
    wrongAnswerMark = models.IntegerField(default=-1)
    time = models.IntegerField(null=True) 
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    

    def __str__(self):
            return self.name

    class Meta:
        ordering=["-created","-updated"]

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=200,null=False)

    def __str__(self):
            return self.name
            
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,null=False)
    name = models.CharField(max_length=200,null=False)
    isCorrect = models.BooleanField(default=False)

    def __str__(self):
            return self.name

class Attempt(models.Model):
     quizTaker = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,null=False)
     score = models.IntegerField(null=True)

class Answer(models.Model):
     question = models.ForeignKey(Question, on_delete=models.CASCADE,null=False)
     attempt = models.ForeignKey(Attempt, on_delete=models.CASCADE,null=False)
     options = models.ManyToManyField(
     Choice, related_name='options', blank=True)