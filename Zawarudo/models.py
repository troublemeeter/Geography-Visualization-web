from django.db import models

# Create your models here.

class Animation(models.Model):
    name = models.CharField(max_length=64)
    uid = models.IntegerField()
    statics = models.TextField()

    def __str__(self):
        return self.name


class tb(models.Model):
    user = models.CharField(max_length=32)
