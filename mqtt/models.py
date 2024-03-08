from django.db import models

class Mq(models.Model):
    idmqtt = models.ForeignKey("Do", on_delete=models.CASCADE, default=None)
    nom = models.CharField(max_length=100)
    piece = models.CharField(max_length=100)
    emplacement = models.CharField(max_length=100)
    mqdate = models.DateField(blank=True, null=True)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine


class Do(models.Model):
    mqid = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    heure = models.CharField(max_length=100, blank=True, null=True)
    temp = models.FloatField(blank=True, default=None)

    mqnom = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        chaine = f"{self.mqid}"
        return chaine






    

    