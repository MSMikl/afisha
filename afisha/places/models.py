from django.db import models
from tinymce.models import HTMLField

import afisha.settings as settings


class Place(models.Model):
    title = models.CharField('Название', max_length=200, blank=False)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    longitude = models.FloatField('Долгота', null=True)
    latitude = models.FloatField('Широта', null=True)

    def __str__(self):
        return self.title


class Image(models.Model):

    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    url = models.ImageField('Картинка')
    order_number = models.IntegerField(
        'Порядковый номер',
        default=0,
        blank=False,
        null=False,
        db_index=True
    )

    def get_last_number(self):
        return self.objects.last().order_number

    def __str__(self):
        return f"{self.order_number} {self.place.title}"

    @property
    def absolute_image_url(self):
        return f"{settings.MEDIA_URL}{self.url}"

    class Meta:
        ordering = ['order_number']
