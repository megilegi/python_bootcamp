from django.db import models

# Create your models here.

class Engine(models.Model):
    pojemnosc = models.CharField(max_length=255)
    ilosc_cylindrow = models.CharField(max_length=255)
    cykl_spalania = models.CharField(max_length=255)


    def __str__(self):
        return str(self.id) + " | " + self.pojemnosc + " | " + self.ilosc_cylindrow + " | " + self.cykl_spalania
