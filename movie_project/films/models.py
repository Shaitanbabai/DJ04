from django.db import models


class Film(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    description = models.TextField()
    review = models.TextField()

    def __str__(self):
        return self.title
