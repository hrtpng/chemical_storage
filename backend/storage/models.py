from django.db import models


class Compound(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    formula = models.CharField(max_length=100)
    iupac = models.CharField(max_length=200, null=True, blank=True)
    cas = models.CharField(max_length=30, null=True, blank=True)
    tags = models.CharField(max_length=200, null=True, blank=True)
    shelf = models.CharField(max_length=10)
    rack = models.CharField(max_length=10)
