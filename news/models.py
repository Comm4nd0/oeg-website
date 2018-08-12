from django.db import models

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=250)
    image = models.ImageField(blank=True)
    attachment = models.FileField(blank=True)
    date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title