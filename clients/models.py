from statistics import mode
from django.db import models


class Client(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
