from django.contrib import admin
from .models import *
# Register your models here.

# -- enregistrement des experts au niveau de la zone admin --
admin.site.register(Expert)

# -- enregistrement des questions au niveau de la zone admin --
admin.site.register(Question)

# -- enregistrement des réponses au niveau de la zone admin --
admin.site.register(Reponse)