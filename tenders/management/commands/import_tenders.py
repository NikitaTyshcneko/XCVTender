# Django management command to create dummy tenders
from django.core.management.base import BaseCommand

from libs.tenders_guru.client import tenders_guru_client
from tenders.models import Tender


class Command(BaseCommand):
    help = 'Import tenders from tenders guru'

    def handle(self, *args, **kwargs):
        for tender in tenders_guru_client.get_tenders():
            obj, created = Tender.objects.get_or_create(
                tender_id=tender['id'],
            )

            if obj:
                obj.name = tender['title']
                obj.description = tender['description']
                obj.category = tender['category']
                obj.euro_value = tender['awarded_value_eur']
                obj.save()
            self.stdout.write(self.style.SUCCESS(f"Successfully created dummy tender - {tender['title']}"))
