# from django.db import models

# # Create your models here.
# class Url(models.Model):
#     url = models.URLField(max_length=150)
#     shorten = models.URLField(max_length=150)

#     def __str__(self):
#         return self.url, self.shorten


from django.db import models
from hashlib import md5

class UrlData(models.Model):
    url = models.URLField(max_length=200, unique=True)
    short = models.URLField(max_length=15, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:10]

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"Short Url for: {self.url} is {self.short}"


# Above Code Creates a Table UrlData in our Database with Columns url, slug. We will use url column to store Original URL and slug to store 10-character string which will be used for shortening the URL.

