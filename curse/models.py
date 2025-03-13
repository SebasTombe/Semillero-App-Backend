from django.db import models

class Modulo(models.Model):
    Area = models.CharField(max_length=100)
    NombreModulo = models.CharField(max_length=100)
    DescripcionModulo = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.Area} - {self.NombreModulo}"
