import json
import os

from services_api.api.optimal_package import OptimalPackage, Package
from services_api.api.request_func import request_func


class ApiLKP:
    def __init__(self, api_token=None, test=False):
        if test:
            self.url = os.getenv('LKP_API_URL_TEST')
        else:
            self.url = os.getenv('LKP_API_URL')
        if api_token:
            self.api_token = api_token
        else:
            self.api_token = os.getenv('LKP_API_STANDARD_TOKEN')

    def get_order_data(self, num):
        data = request_func(
            f'http://calc-support-api.boxberry.ru/parcel/{num}?expand=data',
            headers={'Authorization': 'Bearer Ir7eeghugetohchoyeimareehiereedi-token'}
            )
        return data if data else self.data_from_ml(num)

    def data_from_ml(self, num):
        data = request_func(
            f'https://middle-aggregator.boxberry.ru/v1/parcel?trackNumbers={num}',
            headers={
                'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhbnl3aGVyZSIsImlzcyI6IlNoaXNocGFyZW5vayBWbGFkaW1pciIsIlRva2VuVHlwZSI6Im1hbnVhbCBnZW4iLCJFbnZUeXBlIjoicHJvZCIsIkNsaWVudENvZGUiOiJMS1AiLCJLaW5kIjoiQm94YmVycnlJbnRlcm5hbCJ9.RZFcBbRHuSlkrlRXWxZ2_bUZ4SjZAYatD2L7D4NGYNLn4lCkvwJJfwipSb98LubfE_JnBFwXmRTkhFjOabN9sq8yZlkc_80AFtyIYrSrN21m536QcLg25BpulJAlyQ_USvAsoKPMYjBIowfVJEsdo2M-bFQcwvLPLLwGMaxIe0y8nteBRPaqwVuOfQ-Zxrq_dbjJlp4TgOR3pBThbP0xW9L1YtdMRUfcEfKf2U3Y7-JeDrICJSgnoArmmZdodjR-cUIciUgeKkVqJtHzB4NoHkE_vMPCerLWi2eijZC7oYu6H3To4gXzSNJB_JAQSzeFHL0hL56jLWu68fIew_q-Y1Uaca_kWINOBoSBJ4IQ6ng8H-NqyQLXNsGM3Q45DCry54YVEB-pnIaRTgUkn2HOeroBRaz5qBy5nkp0wiOb-yat8qTm7wb6Bh_YA-YIyZCdV2y2vYMq6g6x8HvC0LmmgV3onYVo9IIo5L1daqDqhmXUy-p-1BD_pSconfIT3eL8hrl64pONcZ5SmyNMfDsXgNP8okWuYboMtBb5dW-YW2O68ysYEl4HyFFOKPpPtAVT7bUQUnP9aTD9bKvZnmCXgwtlhWjDfpKG6dv-quZ_0zKQKhgmSbOMqm02Id_AdiaQcrRbwaZWeTxEYTCcYFXeWAzMJcCXaxskzL7HW-FetvY'
            }
        )
        return self.parse_request_from_ml(data)


    def parse_request_from_ml(self, data):
        return {
            'data': {
                'sender': {'city': self.get_city_from_point_code(code=data['parcels'][0]['pointStartCode'])},
                'receiver': {'city':  self.get_city_from_point_code(code=data['parcels'][0]['pointStopCode'])},
                'package': {'package_id': self.get_packages(data=data['barcodes'])},
            }
        }

    def get_city_from_point_code(self, code):
        data = request_func(
            f'https://middle-aggregator-predprod.middle-task.boxberry.ru/v1/points?code={code}',
            headers={
                'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJhbnl3aGVyZSIsImlzcyI6IlNoaXNocGFyZW5vayBWbGFkaW1pciIsIlRva2VuVHlwZSI6Im1hbnVhbCBnZW4iLCJFbnZUeXBlIjoicHJvZCIsIkNsaWVudENvZGUiOiJMS1AiLCJLaW5kIjoiQm94YmVycnlJbnRlcm5hbCJ9.RZFcBbRHuSlkrlRXWxZ2_bUZ4SjZAYatD2L7D4NGYNLn4lCkvwJJfwipSb98LubfE_JnBFwXmRTkhFjOabN9sq8yZlkc_80AFtyIYrSrN21m536QcLg25BpulJAlyQ_USvAsoKPMYjBIowfVJEsdo2M-bFQcwvLPLLwGMaxIe0y8nteBRPaqwVuOfQ-Zxrq_dbjJlp4TgOR3pBThbP0xW9L1YtdMRUfcEfKf2U3Y7-JeDrICJSgnoArmmZdodjR-cUIciUgeKkVqJtHzB4NoHkE_vMPCerLWi2eijZC7oYu6H3To4gXzSNJB_JAQSzeFHL0hL56jLWu68fIew_q-Y1Uaca_kWINOBoSBJ4IQ6ng8H-NqyQLXNsGM3Q45DCry54YVEB-pnIaRTgUkn2HOeroBRaz5qBy5nkp0wiOb-yat8qTm7wb6Bh_YA-YIyZCdV2y2vYMq6g6x8HvC0LmmgV3onYVo9IIo5L1daqDqhmXUy-p-1BD_pSconfIT3eL8hrl64pONcZ5SmyNMfDsXgNP8okWuYboMtBb5dW-YW2O68ysYEl4HyFFOKPpPtAVT7bUQUnP9aTD9bKvZnmCXgwtlhWjDfpKG6dv-quZ_0zKQKhgmSbOMqm02Id_AdiaQcrRbwaZWeTxEYTCcYFXeWAzMJcCXaxskzL7HW-FetvY'
            }
        )
        return data['cityCode']

    def calculation_lap(self, route, package, tariff_delivery_type=4):
        price = 50000
        body = {
            'api_token': self.api_token,
            'method': 'CalculationLaP',
            'public_price': price,
            'sender_city': route.sender_city,
            'receiver_city': route.receiver_city,
            'package': {
                'boxberry_package': 1,
                'package_code': package.code,
            },
        }
        response = request_func(method='POST', url=f'{self.url}?method=CalculationLaP', data=json.dumps(body))
        if response and response.get('data'):
            for delivery_type in response['data']:
                if int(tariff_delivery_type) == int(delivery_type['delivery_type']):
                    return {'price': delivery_type.get('price')/100, 'time': delivery_type.get('time')}
        sss = 12

    def get_packages(self, data):
        pass


    def get_status_code(self, order_num):
        body = {
            'api_token': self.api_token,
            'tracking': order_num
        }
        response = request_func(url=f'{self.url}?method=ListStatuses', data=json.dumps(body))
        if response and response.get('data'):
            status_code = response['data'].get('code')
            if status_code:
                if 10 < int(status_code) <= 140:
                    return 77
                elif int(status_code) >= 160:
                    return 160
                else:
                    return int(status_code)


    def get_status_code_list(self, orders):
        result = {}
        orders = list(orders.values_list('num', flat=True))
        for offset in range(10):
            body = {
                'api_token': self.api_token,
                'parcels': orders[offset: (offset + 1) * 100]
            }
            response = request_func(url=f'{self.url}?method=ListParcelsHist', data=json.dumps(body), timeout=120)
            if response and response.get('data'):
                for item in response.get('data'):
                    history = response.get('data')[item].get('history')
                    if history and len(history) > 1:
                        status_code = int(history[0]['code'])
                    else:
                        status_code = 10
                    if 10 < status_code <= 140:
                        status_code = 77
                    elif status_code >= 160:
                        status_code = 160
                    result[item] = status_code
        return result