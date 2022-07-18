import os

import requests

from django.core.management.base import BaseCommand, CommandError

import afisha.settings as settings

from places.models import Place, Image

class Command(BaseCommand):
    help = 'Add new locations '

    def add_arguments(self, parser):
        parser.add_argument(
            'json_url',
            help='Ссылка на json-файл с информацией о локации'
        )

    def handle(self, *args, **options):
        response = requests.get(options['json_url'])
        response.raise_for_status()
        place_data = response.json()
        place, created = Place.objects.get_or_create(
            title=place_data['title'],
            defaults={
                'description_short': place_data.get('description_short'),
                'description_long': place_data.get('description_long'),
                'longitude': place_data.get('coordinates', {'lng': 0}).get('lng'),
                'latitude': place_data.get('coordinates', {'lat': 0}).get('lat')
            }
        )
        if not created:
            print('Такая локация уже есть')
            return
        for number, image_url in enumerate(place_data.get('imgs')):
            response = requests.get(image_url)
            response.raise_for_status()
            with open(os.path.join(
                    '.',
                    settings.MEDIA_URL,
                    os.path.basename(image_url)
                ), 'wb') as file:
                file.write(response.content)
            Image.objects.get_or_create(
                url=os.path.basename(image_url),
                defaults={
                    'place': place,
                    'order_number': number
                }
            )




