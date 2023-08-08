from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    explanation = models.CharField(max_length=500)

    def __str__(self):
        return self.name