from django import forms
from .models import Survey, SurveyQuestion

class SurveyForm(forms.ModelForm):
    name = forms.CharField(
        label='Name',
    )

    class Meta:
        model = Survey
        fields = ['name']

class SurveyQuestionForm(forms.ModelForm):
    question = forms.CharField(
        label='Question',
    )

    class Meta:
        model = SurveyQuestion
        fields = ['type','question']