import os

import requests

from django.core.management.base import BaseCommand

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
        place_details = response.json()
        place, created = Place.objects.get_or_create(
            title=place_details['title'],
            defaults={
                'description_short': place_details.get('description_short'),
                'description_long': place_details.get('description_long'),
                'longitude': place_details.get('coordinates', {'lng': 0}).get('lng'),
                'latitude': place_details.get('coordinates', {'lat': 0}).get('lat')
            }
        )
        if not created:
            print('Такая локация уже есть')
            return
        for number, image_url in enumerate(place_details.get('imgs')):
            response = requests.get(image_url)
            response.raise_for_status()
            with open(os.path.join(
                        '.',
                        settings.MEDIA_URL,
                        os.path.basename(image_url)
                    ), 'wb') as file:
                file.write(response.content)
            Image.objects.get_or_create(
                file=os.path.basename(image_url),
                defaults={
                    'place': place,
                    'order_number': number
                }
            )




