from django.db import models

# Create your models here.
class Url(models.Model):
    original_url = models.URLField(max_length=200)
    shorten = models.CharField(max_length=100, default="w8dj03lsj")

    def __str__(self):
        return self.original_url
