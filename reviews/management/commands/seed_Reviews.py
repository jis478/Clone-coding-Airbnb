import random
from django.core.management.base import BaseCommand
from reviews.models import Review as review_model
from users.models import User as user_model
from rooms.models import Room as room_model
from django_seed import Seed

NAME = "review"


class Command(BaseCommand):

    help = f"Create fake {NAME} data"

    def add_arguments(self, parser):

        parser.add_argument("--number", type=int, default=1, help=f"how many {NAME}s?")

    def handle(self, *args, **kwargs):

        number = kwargs["number"]

        user = user_model.objects.all()  # Non-abstract model
        room = room_model.objects.all()  # Non-abstract model

        seeder = Seed.seeder()
        seeder.add_entity(
            review_model,
            number,
            {
                "accuracy": lambda x: random.randint(0, 6),
                "communication": lambda x: random.randint(0, 6),
                "cleanliness": lambda x: random.randint(0, 6),
                "location": lambda x: random.randint(0, 6),
                "checkin": lambda x: random.randint(0, 6),
                "value": lambda x: random.randint(0, 6),
                "user": lambda x: random.choice(user),
                "room": lambda x: random.choice(room),
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME}(s) created"))
