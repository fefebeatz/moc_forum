from .models import *
from rest_framework import serializers, validators

# -- serializer des experts --
class ExpertListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = ['id', 'nom_expert', 'email', "fonction", "connected_at"]  
        
        
# -- serializers pour l'enregistrement des experts --
class ExpertRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expert
        fields = ('id', 'nom_expert', 'email', "fonction", "connected_at")
    
class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id', 'libelle', 'expert',]
    
    def to_representation(self, instance):
        rep = super(QuestionSerializer,
                    self).to_representation(instance)
        rep['expert'] = instance.expert.nom_expert
        return rep

class ReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = ['id', 'libelle', 'expert', 'question']
    
    def to_representation(self, instance):
        rep = super(ReponseSerializer,
                    self).to_representation(instance)
        rep['expert'] = instance.expert.nom_expert
        rep['question'] = instance.question.libelle
        return rep