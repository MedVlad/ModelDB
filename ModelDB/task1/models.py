from django.db import models
from django.db.models import Model


# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=2, max_digits=6)
    age = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    size = models.PositiveBigIntegerField()
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(to=Buyer)

    def __str__(self):
        return self.title
