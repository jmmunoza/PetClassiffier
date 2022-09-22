from turtle import title
from django.db import models

# Create your models here.
class MLModels(models.Model):
    title = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=100, default=None)
    architecture = models.FileField(upload_to= 'mlmodels/', default=None)
    weights = models.FileField(upload_to= 'mlmodels/', default=None)
    priority = models.PositiveSmallIntegerField(null=True)