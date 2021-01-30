from django.db import models

# Create your models here.

class TestModel(models.Model):
    time = models.IntegerField()

    def __str__(self):
        return str(self.time)