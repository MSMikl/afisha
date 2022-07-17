from django.http.response import JsonResponse
from django.shortcuts import render

from places.models import Place, Image


def index(request):
    data = {'data' : {
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
            "detailsUrl": "./static/places/moscow_legends.json"
          }
        }
        for place in Place.objects.all()
      ]
    }}
    return render(request, "index.html", context=data)


def place(request, place_id):
    place = Place.objects.get(id=place_id)
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
