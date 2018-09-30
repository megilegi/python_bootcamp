from django.db import models


# Create your models here.

class Car(models.Model):
    rok_produkcji = models.IntegerField(default=0000)
    marka = models.CharField(max_length=255, default='marka')
    model_auta = models.CharField(max_length=255, default='model')
    typ_nadwozia = models.CharField(max_length=255, default='nadwozie')
    engine = models.ForeignKey("engines.Engine", blank=True, null=True, on_delete=models.CASCADE)
    fotka = models.ImageField(default = 'brak fotki')

    def __str__(self):
        return str(self.id) + " | " + str(self.rok_produkcji) + " | " + self.marka + " | " + self.typ_nadwozia
