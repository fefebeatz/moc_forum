from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

# -- enregistrement des experts -- 
from rest_framework import status

# -- Création de l'expert --
class ExpertCreateView(APIView):
    def post(self, request):
        serializer = ExpertRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# -- afficher les experts -- 
@api_view(['GET'])
def ListExpertAPIView(request):
    expert = Expert.objects.all()
    serializer = ExpertRegisterSerializer(expert, many=True)
    return Response(serializer.data)


# -- Création de la question --
class QuestionCreateView(APIView):
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# -- afficher les questions -- 
@api_view(['GET'])
def ListQuestionAPIView(request):
    question = Question.objects.all()
    serializer = QuestionSerializer(question, many=True)
    return Response(serializer.data)


# -- Création de la réponse --
class ReponseCreateView(APIView):
    def post(self, request):
        serializer = ReponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# -- afficher les réponses -- 
@api_view(['GET'])
def ListReponseAPIView(request):
    reponse = Reponse.objects.all()
    serializer = ReponseSerializer(reponse, many=True)
    return Response(serializer.data)


# -- afficher un expert par son nom --
class ExpertDetailApiView(APIView):

    def get_object(self, nom_expert):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Expert.objects.get(nom_expert__contains = nom_expert)
        except Expert.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, nom_expert, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        expert_instance = self.get_object(nom_expert)
        if not expert_instance:
            return Response(
                {"res": "Aucun expert avec nom n'a été trouvé"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ExpertListSerializer(expert_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# -- afficher une question par son libelle --
class QuestionDetailApiView(APIView):

    def get_object(self, libelle):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Question.objects.get(libelle__contains = libelle)
        except Question.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, libelle, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        question_instance = self.get_object(libelle)
        if not question_instance:
            return Response(
                {"res": "Aucune question n'a été trouvé"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = QuestionSerializer(question_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
