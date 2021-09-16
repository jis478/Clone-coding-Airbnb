from django.db import models


class TimeStampedModel(models.Model):

    """Time stamped model"""

    created = models.DateField()
    updated = models.DateField()

    class Meta:
        abstract = True
