import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from reservations.models import Reservation as reservation_model
from users.models import User as user_model
from rooms.models import Room as room_model
from django_seed import Seed

NAME = "reservation"


class Command(BaseCommand):

    help = f"Create fake {NAME} data"

    def add_arguments(self, parser):

        parser.add_argument("--number", type=int, default=1, help=f"how many {NAME}?")

    def handle(self, *args, **kwargs):

        number = kwargs["number"]

        user = user_model.objects.all()  # Non-abstract model
        room = room_model.objects.all()  # Non-abstract model

        seeder = Seed.seeder()
        seeder.add_entity(
            reservation_model,
            number,
            {
                "status": lambda x: random.choice(["Pending", "Confirmed", "Canceled"]),
                "guest": lambda x: random.choice(user),
                "room": lambda x: random.choice(room),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(1, 7)),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} {NAME}(s) created"))
