from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    isAvailable = models.BooleanField(default=True)
    # model_pic = models.ImageField(default = '/static/img/no-img.jpg')

    def __str__(self):
        return str(self.name)
