from django.db import models


class TimeStampedModel(models.Model):

    """Time stamped model"""

    created = models.DateField(auto_now_add=True,null=True, blank=True)
    updated = models.DateField(auto_now=True,null=True, blank=True)

    class Meta:
        abstract = True
