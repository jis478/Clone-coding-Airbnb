from django.db import models
from django.utils import timezone
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    """Reservation Model Defitnition"""

    STATUS_PENDING = "Pending"
    STATUS_CONFIRMED = "Confirmed"
    STATUS_CANCELED = "Canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELED, "Canceled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )

    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)

    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    check_in = models.DateField()
    check_out = models.DateField()

    # def __str__(self):
    #     return f"{self.room} - {self.check_in}"

    def __str__(self):
        return f"{self.room}"

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    is_finished.boolean = True

    
