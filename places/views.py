from django.http import JsonResponse
from .models import Place


def place_details(request, place_id):
    place = Place.objects.prefetch_related("images").get(id=place_id)

    data = {
        "title": place.title,
        "imgs": [img.image.url for img in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.lng, "lat": place.lat},
    }

    return JsonResponse(data)
