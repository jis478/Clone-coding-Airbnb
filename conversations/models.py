from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    partipicants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        partipicants = self.partipicants.all()  # QuerySet (many to many fields)
        usernames = []
        for p in partipicants:
            usernames.append(p.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.partipicants.count()

    count_participants.short_description = "Number of Partipicants"


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says:{self.message}"
