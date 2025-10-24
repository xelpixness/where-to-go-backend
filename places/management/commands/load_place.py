import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = "Load place from JSON URL"

    def add_arguments(self, parser):
        parser.add_argument("json_url", type=str, help="URL to JSON file")

    def handle(self, *args, **options):
        json_url = options["json_url"]

        try:
            response = requests.get(json_url)
            response.raise_for_status()
            place_data = response.json()

            place, created = Place.objects.get_or_create(
                title=place_data["title"],
                defaults={
                    "description_short": place_data.get("description_short", ""),
                    "description_long": place_data.get("description_long", ""),
                    "lng": float(place_data["coordinates"]["lng"]),
                    "lat": float(place_data["coordinates"]["lat"]),
                },
            )

            for img_url in place_data.get("imgs", []):
                img_response = requests.get(img_url)
                img_response.raise_for_status()

                img_name = img_url.split("/")[-1]
                place_image = PlaceImage(place=place)
                place_image.image.save(
                    img_name, ContentFile(img_response.content), save=True
                )

            action = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"{action} place: {place.title}"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error loading place: {e}"))
