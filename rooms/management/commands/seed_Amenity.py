from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    # help = "this is a help test"

    # def add_arguments(self, parser):

    #     parser.add_argument("option", type=int, help="test")

    def handle(self, *args, **kwargs):

        #     print(kwargs["option"])

        amenities = ["Sofa", "TV", "Bathtub"]

        for a in amenities:
            Amenity.objects.create(name=a)

        self.stdout.write(self.style.SUCCESS("Amenities added"))
