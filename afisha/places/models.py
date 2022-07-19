from django.db import models
from tinymce.models import HTMLField

import afisha.settings as settings


class Place(models.Model):
    title = models.CharField('Название', max_length=200, blank=False)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = HTMLField('Полное описание', blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'


class Image(models.Model):

    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Локация'
    )
    file = models.ImageField('Картинка')
    order_number = models.IntegerField(
        'Порядковый номер',
        default=0,
        db_index=True
    )

    class Meta:
        ordering = ['order_number']
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


    def __str__(self):
        return f"{self.order_number} {self.place.title}"

    @property
    def absolute_image_url(self):
        return f"/{settings.MEDIA_URL}{self.file}"

