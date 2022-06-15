from django.shortcuts import render, redirect
from django.views import View
from .forms import SurveyForm, SurveyQuestionForm
from .models import Survey, SurveyAnswer, SurveyQuestion, UnregisteredUserEmail
from django.contrib import messages
from django.http import JsonResponse
import json

# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            surveys = Survey.objects.exclude(user__in = [request.user])
        else:
            surveys = Survey.objects.all()
        context = {
            'surveys': surveys
        }
        return render(request, 'app/index.html', context)

class CreateSurvey(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': SurveyForm()
        }
        return render(request, 'app/createSurvey.html', context)

    def post(self, request, *args, **kwargs):
        form = SurveyForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            new_survey = form.save()
            return redirect('add-question', pk = new_survey.pk)
        
        return render(request, 'app/createSurvey.html', context)


class AddQuestion(View):
    def get(self, request, pk, *args, **kwargs):
        survey = Survey.objects.get(pk = pk)
        questions = survey.questions.all() 
        context = {
            'form': SurveyQuestionForm(),
            'number_of_question': len(questions),
            'survey': survey 
        }
        return render(request, 'app/addQuestion.html', context)

    def post(self, request, pk, *args, **kwargs):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        form = SurveyQuestionForm(request.POST)
        print(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            option1 = request.POST.get('option1', None)
            option2 = request.POST.get('option2', None)
            option3 = request.POST.get('option3', None)
            option4 = request.POST.get('option4', None)
            new_question.option1 = option1
            new_question.option2 = option2
            new_question.option3 = option3
            new_question.option4 = option4
            new_question.save()

            survey = Survey.objects.get(pk = pk)
            survey.questions.add(new_question)
            if is_ajax:
                return JsonResponse({'Success': True})
            messages.success(request, 'Survey Created Successfully')
            return redirect('index')
        messages.error(request, 'Internal Error. Please Try Later')
        return redirect('index')

class GiveSurvey(View):
    def get(self, request, pk, *args, **kwargs):
        survey = Survey.objects.get(pk = pk)
        context = {
            "survey": survey,
            "ranking": ['worst', 'bad', 'good', 'better', 'best'],
        }
        print(context)
        return render(request, 'app/giveSurvey.html', context)

    def post(self, request, pk, *args, **kwargs):
        survey = Survey.objects.get(pk = pk)
        if request.user.is_authenticated:
            survey.user.add(request.user)
        else: 
            email = UnregisteredUserEmail.objects.create(email = request.POST['email'])
            survey.userEmail.add(email)
        questions = survey.questions.all()
        for question in questions:
            if request.POST.get(str(question.pk), None):
                if request.user.is_authenticated:
                    SurveyAnswer.objects.create(question = question, answer = request.POST[str(question.pk)], user = request.user )
                else:
                    SurveyAnswer.objects.create(question = question, answer = request.POST[str(question.pk)], userName = request.POST['name'], userEmail = request.POST['email'] )
        return redirect('index')

class UnregisteredEmailVerification(View):
    def post(self, request, pk, *args, **Kwargs):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            survey = Survey.objects.get(pk = pk)
            emailList = survey.userEmail.all()
            body_unicode = request.body.decode('utf-8')
            email = json.loads(body_unicode)
            for mail in emailList:
                if mail.email == email:
                    return JsonResponse({'Success': True})
            return JsonResponse({'Success': False})
        return JsonResponse({'Error': 'Internal Error'})