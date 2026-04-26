from django.management.base import BaseCommand

class Command(BaseCommand):
    help = "Seed Products data into the database"

    @transaction.atomic
    def handle(self, *args, **options):
        