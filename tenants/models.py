from django.db import models

# Create your models here.


class UnitModel(models.Model):
    title = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self) -> str:
        return self.title