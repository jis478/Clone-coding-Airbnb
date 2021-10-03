from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    # help = "this is a help test"

    # def add_arguments(self, parser):

    #     parser.add_argument("option", type=int, help="test")

    def handle(self, *args, **kwargs):

        #     print(kwargs["option"])

        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for a in facilities:
            Facility.objects.create(name=a)

        self.stdout.write(self.style.SUCCESS("Facilities added"))
