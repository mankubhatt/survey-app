from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Survey(models.Model):
    name = models.CharField(max_length=100)
    questions = models.ManyToManyField('SurveyQuestion')
    user = models.ManyToManyField(User, blank = True)
    userEmail = models.ManyToManyField('UnregisteredUserEmail', blank = True)

class UnregisteredUserEmail(models.Model):
    email = models.EmailField(null = True, blank = True)


class SurveyQuestion(models.Model):
    choices = [
        ("1", "Rating"),
        ("2", "Mcq"),
        ("3", "Ranking"),
        ("4", "Value Based"),
    ]
    question = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=choices)
    option1 = models.CharField(max_length=100, null = True, blank = True)
    option2 = models.CharField(max_length=100, null = True, blank = True)
    option3 = models.CharField(max_length=100, null = True, blank = True)
    option4 = models.CharField(max_length=100, null = True, blank = True)
    answer = models.CharField(max_length=100, null = True, blank = True)

class SurveyAnswer(models.Model):
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank= True)
    userName = models.CharField(max_length=100)
    userEmail = models.EmailField()