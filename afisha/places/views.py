from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse

from places.models import Place


def index(request):
    data = {'data': {
      "type": "FeatureCollection",
      "features": [
        {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.longitude, place.latitude]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse(viewname='place_json', args=[place.id])
          }
        }
        for place in Place.objects.all()
      ]
    }}
    return render(request, "index.html", context=data)


def place(request, place_id):
    place = Place.objects.filter(id=place_id).select_related().last()
    data = {
        "title": place.title,
        "imgs": [str(image.absolute_image_url) for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": str(place.longitude),
            "lat": str(place.latitude)
        }
    }
    return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False, 'indent': 2})
