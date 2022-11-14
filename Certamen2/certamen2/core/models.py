from django.db import models


class residencia(models.Model):
    NRO = models.CharField(max_length = 30)
    DUEÑO = models.CharField(max_length = 30)
    fono_dueño = models.CharField(max_length = 30)
    



class correspondencia(models.Model):
    fecha_recepcion = models.DateField()
    remitente = models.CharField(max_length=30)
    conserje = models.CharField(max_length=30)
    destinatario = models.CharField(max_length=30)
    numero_res = models.ForeignKey(residencia, on_delete=models.CASCADE)
    estado = models.CharField(max_length=30)

    def __str__(self):
        return "Dueño "+ str(self.remitente)
