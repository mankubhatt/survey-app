from django.urls import path
from .views import Index, CreateSurvey, AddQuestion, GiveSurvey, UnregisteredEmailVerification

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('create-survey/', CreateSurvey.as_view(), name='create-survey'),
    path('add-question/<int:pk>/', AddQuestion.as_view(), name='add-question'),
    path('give-survey/<int:pk>/', GiveSurvey.as_view(), name='give-survey'),
    path('email-verify/<int:pk>/', UnregisteredEmailVerification.as_view(), name='email-verify'),
]
