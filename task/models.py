from django.db import models


class Task(models.Model):
    def __str__(self):
        return f'Name: {self.name}\t Category: {self.category}'

    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)