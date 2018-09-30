from django.db import models
from colorfield.fields import ColorField

# Create your models here.

CONTAINER_TYPES = (
    ("glassbottle", "Glass Bottle"),
    ("plasticbottle", "Plastic Bottle"),
    ("box", "Box")

)


class Container(models.Model):
    type = models.CharField(choices=CONTAINER_TYPES, max_length=50)
    colour = ColorField(default='#FF0000')

    def __str__(self):
        return f"{self.type}, {self.colour}"
