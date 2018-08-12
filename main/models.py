from django.db import models


class Banner(models.Model):
    image = models.FileField()
    title = models.CharField(max_length=50, blank=True)
    text = models.TextField(blank=True)
    url = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title