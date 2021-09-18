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

    pass


class Amenity(AbstractItem):

    pass


class Facility(AbstractItem):

    pass


class HouseRule(AbstractItem):

    pass


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
        user_models.User, on_delete=models.CASCADE, null=True, blank=True
    )
    roomtype = models.ForeignKey(
        RoomType,
        on_delete=models.SET_NULL,
        null=True,
    )
    amenities = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
