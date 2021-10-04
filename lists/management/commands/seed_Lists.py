import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from lists.models import List as list_model
from users.models import User as user_model
from rooms.models import Room as room_model
from django_seed import Seed

NAME = "list"


class Command(BaseCommand):

    help = "Create fake review data"

    def add_arguments(self, parser):

        parser.add_argument("--number", type=int, default=1, help=f"how many {NAME}?")

    def handle(self, *args, **kwargs):

        number = kwargs["number"]

        user = user_model.objects.all()  # Non-abstract model
        room = room_model.objects.all()  # Non-abstract model

        seeder = Seed.seeder()
        seeder.add_entity(
            list_model,
            number,
            {
                "user": lambda x: random.choice(user),
                # "rooms": lambda x: random.choice(room),
            },
        )

        created_list = seeder.execute()  # return pks
        cleaned = flatten(list(created_list.values()))

        for pk in cleaned:
            list_object = list_model.objects.get(pk=pk)
            room_added = room[
                random.randint(0, 2) : random.randint(10, 15)
            ]  # return sliced filedset query (room)
            list_object.rooms.add(*room_added)

        self.stdout.write(self.style.SUCCESS(f"{number} {NAME}(s) created"))
