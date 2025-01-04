from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    desc = models.TextField(max_length=250, blank=True)

    def __str__(self):
        return self.name
