from django.db import models
from django.db.models.constraints import CheckConstraint
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    checkin = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_avg(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.checkin
            + self.value
        ) / 6
        return round(avg, 2)

    rating_avg.short_description = "AVG."
