import json
import traceback

from datetime import datetime

from partner.models import Partner
from src.services_api.api.lkp import ApiLKP
from src.services_api.api.s3client import S3Client
from statistic.models import Package, Statistic, Route


def update_statistic():
    for _ in range(10):
        messages = S3Client().get_messages_from_queue()
        if messages:
            for n, message in enumerate(messages[:-1]):
                status = json.loads(message['Body'])
                if not status['track'].startswith('00002'):
                    # try:
                        order_data = ApiLKP().get_order_data(num=status['track'])
                        date = datetime.fromtimestamp(status['statusTime'])
                        partner, create = Partner.objects.get_or_create(token=order_data['data'].get('api_key', 'pip'))
                        route, create = Route.objects.get_or_create(
                            sender=order_data['data']['sender']['city'],
                            receiver=order_data['data']['receiver']['city'],
                        )
                        package = Package.objects.get(code=order_data['data']['package']['package_id'])
                        Statistic.manager.update_statistic(date=date, status=status, partner=partner,
                                                           route=route, package=package)
                    # except:
                    #     print(traceback.format_exc())
                print(n)
                try:
                    S3Client().delete_message_from_queue(message)
                except:
                    print(traceback.format_exc())
                    ss = 1