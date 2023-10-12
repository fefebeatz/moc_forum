from django.urls import path
from .views import *

urlpatterns = [
    path('api/register-expert/', ExpertCreateView.as_view(), name='register-expert'),
    path('api/expert/', ListExpertAPIView, name='expert'),
    path('api/register-question/', QuestionCreateView.as_view(), name='register-question'),
    path('api/questions/', ListQuestionAPIView, name='question'),
    path('api/register-reponse/', ReponseCreateView.as_view(), name='register-reponse'),
    path('api/reponses/', ListReponseAPIView, name='reponse'),
    path('api/expert/<str:nom_expert>/', ExpertDetailApiView.as_view()),
    path('api/question/<str:libelle>/', QuestionDetailApiView.as_view()),
]