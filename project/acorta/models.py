from django.db import models

class urls(models.Model):
    url_original = models.CharField(max_length=28)
    url_acortada = models.CharField(max_length=28)
