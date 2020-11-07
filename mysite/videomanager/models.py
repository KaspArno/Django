from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Videos(models.Model):
    name = models.CharField(max_length=150)
    lenght = models.DurationField()
    folder_path = models.CharField(max_length=200)

    def __str__(self):
        return self.name
