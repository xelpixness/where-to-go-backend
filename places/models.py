from django.db import models

from ckeditor.fields import RichTextField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description_short = models.TextField(verbose_name="Краткое описание", blank=True)
    description_long = RichTextField(verbose_name="Полное описание", blank=True)
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")

    def __str__(self):
        return self.title


class PlaceImage(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(verbose_name="Картинка")
    position = models.PositiveIntegerField(
        default=0, verbose_name="Позиция", db_index=True
    )

    class Meta:
        ordering = ["position"]
