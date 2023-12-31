from django.db import models

class Endereco(models.Model):
    linha1 = models.CharField(max_length=255)
    linha2 = models.CharField(max_length=255, blank=True, null=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    latitude = models.IntegerField(blank=True, null=True)
    longitude = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.linha1