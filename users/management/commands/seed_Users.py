from django.core.management.base import BaseCommand
from users.models import User as user_model
from django_seed import Seed


class Command(BaseCommand):

    help = "Create fake user data"

    def add_arguments(self, parser):

        parser.add_argument("--number", type=int, default=1, help="how many users?")

    def handle(self, *args, **kwargs):

        number = kwargs["number"]

        seeder = Seed.seeder()
        seeder.add_entity(
            user_model, number, {"is_staff": False, "is_superuser": False}
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} user(s) created"))
