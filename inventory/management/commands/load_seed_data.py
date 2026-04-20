import json
from pathlib import Path
from django.conf import settings
from django.db import transaction
from django.core.management.base import BaseCommand
from inventory.models import Category,Address

class Command(BaseCommand):
    help = "Seed data into the database"
    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            type=str,
            default="C:/Users/udayk/inventory-management-system/inventory_management_system/inventory/seeds/seed_data.json/",
            help="Path to seed JSON file relative to BASE_DIR",)
        
    @transaction.atomic
    def handle(self, *args, **options):
        file_path = Path(settings.BASE_DIR / options["file"])
        if not file_path.exists():
            self.stdout.write(
                self.style.ERROR(f"Seed file not found: {file_path}"))
            return
        with open(file_path,"r",encoding="utf-8") as f:
            data = json.load(f)
        categories_data = data.get("categories",[])
        addresses_data = data.get("addresses",[])

        category_objects = []
        for item in categories_data:
            category_objects.append(
                Category(   name = item["name"],
                description = item["description"],)
             
            )    

        address_objects = []
        for item in addresses_data:
            address_objects.append(
                Address( lane1 = item["lane1"],
                lane2 = item["lane2"],
                city = item["city"],
                state = item["state"],
                country = item["country"],
                pincode = item["pincode"],)
         
            )
        if category_objects:    
            Category.objects.bulk_create(category_objects)
        if address_objects:
            Address.objects.bulk_create(address_objects)
        self.stdout.write(self.style.SUCCESS(f"Seed data loaded successfully: {len(category_objects)} categories, {len(address_objects)} addresses"))