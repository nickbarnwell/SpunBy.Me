from django.db import models

# Create your models here.

class Party(models.Model):
  party_name = models.CharField(max_length=50)

