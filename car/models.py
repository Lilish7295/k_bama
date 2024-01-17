from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    tecnical_info = models.TextField()
    news = models.TextField()
