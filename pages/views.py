from django.shortcuts import render

from places.models import Place
import json


def home_page(request):
    places = Place.objects.all()

    geo_json = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [place.lng, place.lat]},
                "properties": {
                    "title": place.title,
                    "placeId": place.id,
                    "detailsUrl": f"/places/{place.id}/",
                },
            }
            for place in places
        ],
    }

    return render(request, "pages/index.html", {"geo_json": json.dumps(geo_json)})
