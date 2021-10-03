from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item class. Doesn't stay in the database."""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    class Meta:
        verbose_name = "Room Type"


class Amenity(AbstractItem):
    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    class Meta:
        verbose_name = "House Rule"


class Room(core_models.TimeStampedModel):

    name = models.CharField(max_length=140, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=140, null=True, blank=True)
    beds = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    baths = models.IntegerField(null=True, blank=True)
    guests = models.IntegerField(null=True, blank=True)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    instant_book = models.BooleanField(default=False, null=True, blank=True)
    host = models.ForeignKey(
        user_models.User,
        related_name="rooms",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    roomtype = models.ForeignKey(
        RoomType,
        on_delete=models.SET_NULL,
        null=True,
    )
    amenities = models.ManyToManyField(Amenity, related_name="rooms")
    facilities = models.ManyToManyField(Facility, related_name="rooms")
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def total_avg(self):  # bringing review class objects for each room object
        reviews_all = self.reviews.all()
        reviews = 0
        for review in reviews_all:
            reviews += review.rating_avg()
        if len(reviews_all) > 0:
            return round(reviews / len(reviews_all), 2)
        else:
            return 0


class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    room = models.ForeignKey(
        Room, related_name="photos", on_delete=models.CASCADE
    )  # room -> photos, not photos -> room

    def __str__(self):
        return self.caption
