from django.core.management.base import BaseCommand

from src.statistic.services.statistic import update_statistic


class Command(BaseCommand):
    help = 'обновление тарифов'

    def handle(self, *args, **kwargs) -> None:
        update_statistic()