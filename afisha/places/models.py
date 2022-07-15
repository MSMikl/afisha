from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=200, blank=False)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Полное описание', blank=True)
    longitude = models.FloatField('Долгота', null=True)
    lattitude = models.FloatField('Широта', null=True)

    def __str__(self):
        return self.title

# Create your models here.
