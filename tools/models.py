from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    isAvailable = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)
