from django.db import models

class Gallery(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.title