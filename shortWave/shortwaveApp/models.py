from django.db import models

class LinkInfo(models.Model):
    link = models.CharField(max_length=10000)  # Field to store the original link
    link_id = models.CharField(max_length=5, unique=True)  # Field to store the shortened link ID abd Ensure uniqueness of string formed

    def __str__(self):
        return self.link_id
