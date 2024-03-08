# dossiermedical/models.py
from django.db import models

class PredictionInput(models.Model):
    nom = models.CharField(max_length=100, default='nom')
    prenom = models.CharField(max_length=100, default='prenom')
    tel1 = models.CharField(max_length=10, default='0123456789')
    tel2 = models.CharField(max_length=10, default='0123456789')
    email = models.EmailField(default='example@example.com')
    file_upload = models.FileField(upload_to='uploads/', null=True, blank=True)

# other_module.py
from dossiermedical.models import PredictionInput  # Import PredictionInput only when needed

# Continue with the rest of your code...
