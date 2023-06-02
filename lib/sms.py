# Dadmehr - Garfox
# packages
import requests
import random
import json
import re

from fake_useragent import UserAgent
import Banner
range_n_limit = 100
cunt = 0
services = ['rirabook', 'doctoreto']

# +_+_+_+ User Agent Generator +_+_+_+
# ua = UserAgent()
# user_agent = ua.random
# print(user_agent)


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
    with open('./API/sms.json') as json_file:
        data = json.load(json_file)

        # Replace phone number in data
        rep_data = str(data)
        rep_data = rep_data.replace('numnum', phone_number)
        print(phone_number)

    if range_n <= range_n_limit:
        for i in range(1, range_n + 1):
            cunt = i
            for service in services:
                # convert service list to str
                service_name = str(service)
                print(service_name)

                # load apos in sms.json
                url_data = data[service_name]

                url = url_data['url']
                req_data = url_data['data']

                req = requests.post(url=url, data=req_data)
                print(req, cunt)
    else:
        print('Send Range Limit 100')


if __name__ == "__main__":
    banner = Banner.banner()