import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from users.models import User as user_model
from rooms.models import Photo, Room as room_model
from rooms.models import Photo as photo_model

from rooms.models import RoomType as roomtype_model

from django_seed import Seed


class Command(BaseCommand):

    help = "Create fake room data"

    def add_arguments(self, parser):

        parser.add_argument("--number", type=int, default=1, help="how many rooms?")

    def handle(self, *args, **kwargs):

        number = kwargs["number"]

        host = user_model.objects.all()  # Non-abstract model
        roomtype = roomtype_model.objects.all()  # Abstract model

        seeder = Seed.seeder()
        seeder.add_entity(
            room_model,
            number,
            {
                "name": seeder.faker.address(),
                "host": lambda x: random.choice(host),
                "roomtype": lambda x: random.choice(roomtype),
                "price": lambda x: random.randint(30000, 2000000),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
            },
        )
        created_rooms = seeder.execute()
        created_rooms_pk = flatten(list(created_rooms.values()))  # created rooms' pks

        for pk in created_rooms_pk:
            room = room_model.objects.get(pk=pk)
            for i in range(3, random.randint(5, 10)):
                photo_model.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1,31)}.webp",
                )

        self.stdout.write(self.style.SUCCESS(f"{number} room(s) created"))
