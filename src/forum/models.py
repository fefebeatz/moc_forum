from django.db import models

# Create your models here.


# -- modèle expert -- 
class Expert(models.Model):
    nom_expert = models.CharField('Nom de l\'expert', max_length=255)
    email = models.EmailField(unique=True)
    fonction = models.CharField('Fonction', max_length=255)
    connected_at = models.DateField()
    
    def __str__(self):
        return self.nom_expert

# -- modèle question -- 
class Question(models.Model):
    libelle = models.TextField('Libellé de la question')
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='question_expert')
    
    def __str__(self) -> str:
        return self.libelle
    
# -- modèle réponse -- 
class Reponse(models.Model):
    libelle = models.TextField('Libellé de la réponse')
    expert = models.ForeignKey(Expert, on_delete=models.CASCADE, related_name='reponse_expert')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='reponse_question')
    
    def __str__(self) -> str:
        return self.libelle