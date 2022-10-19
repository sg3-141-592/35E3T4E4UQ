from django.db import models

class Site(models.Model):
    source_url = models.CharField(max_length=2048)
    target_url = models.CharField(max_length=2048)
    private_key = models.TextField()
    fullchain_key = models.TextField()

    def __str__(self):
        return f"{self.source_url} - {self.target_url}"
