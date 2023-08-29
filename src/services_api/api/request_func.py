import logging
import traceback
from json.decoder import JSONDecodeError

import requests
import urllib3
import json as json_func
from requests import ReadTimeout

logger = logging.getLogger("app")


def request_func(url, method='GET', params=None, headers=None, json=None, data=None, timeout=3, http=False, body=None, verify=True, need_400=False, to_dict=True, try_count=5):
    response = None
    headers = {"Content-Type": "application/json"} if headers is None else headers
    for _ in range(try_count):
        try:
            if http:
                http = urllib3.PoolManager()
                if body:
                    response = http.request('POST', url, headers=headers, body=body)
                    return json_func.loads(response.data)
            else:
                if method == 'GET':
                    if params:
                        response = requests.get(url=url, params=params, headers=headers, timeout=timeout)
                    elif data:
                        response = requests.get(url=url, data=data, headers=headers, timeout=timeout)
                    else:
                        response = requests.get(url=url, timeout=timeout, headers=headers)
                elif method == 'POST':
                    if params:
                        response = requests.post(url=url, params=params, headers=headers, timeout=timeout)
                    elif json:
                        response = requests.post(url=url, json=json, headers=headers, timeout=timeout)
                    elif data:
                        response = requests.post(url=url, data=data, headers=headers, timeout=timeout, verify=verify)
                    else:
                        response = requests.post(url=url, headers=headers, timeout=timeout, verify=False)
                elif method == 'DELETE':
                    response = requests.delete(url=url, headers=headers)
                if response:
                    if to_dict:
                        try:
                            response = response.json()
                        except JSONDecodeError:
                            pass
                    return response
                elif need_400 and response.status_code == 400:
                    return response.json()
        except ReadTimeout:
            print(f'таймаут: {_ + 1} из {try_count}')
        except:
            print(traceback.format_exc())
