from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_available = models.BooleanField(default=False)
    container = models.ForeignKey("containers.Container", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " | " + self.name
