from django.db import models

# Create your models here.
class Url(models.Model):
    url = models.URLField(max_length=150)
    shorten = models.URLField(max_length=150)

    def __str__(self):
        return self.url, self.shorten