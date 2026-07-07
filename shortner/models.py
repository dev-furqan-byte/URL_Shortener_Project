from django.db import models

class ShortURL(models.Model):
    original_url = models.TextField()
    short_code = models.CharField(max_length=10, unique=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.short_code