# Dadmehr - Garfox
# packages
import requests
import random
from fake_useragent import UserAgent
import json

range_n_limit = 100
cunt = 0
services = ['rirabook', 'doctoreto']

# +_+_+_+ User Agent Generator +_+_+_+
# ua = UserAgent()
# user_agent = ua.random
# print(user_agent)


def send(phone_number, range_n):  # add prvity Change IP
    global cunt  # تعریف متغیر global

    # Load lib/API/sms.json
    with open('./API/sms.json') as json_file:
        data = json.load(json_file)
        rep_data = str(data)
        rep_data.replace('numnum',phone_number)
        print(phone_number)
        print(rep_data)
    if range_n <= range_n_limit:
        cunt = 0
        for service in services:
            cunt += 1

            # convert service list to str
            service_name = str(service)
            print(service_name)

            # load api
            url_data = data[service_name]

            url = url_data['url']
            req_data = url_data['data']


            req = requests.post(url=url, data=req_data)
            print(req, cunt)
    else:
        print('Send Range Limit 100')


send(phone_number='123456789', range_n=100)
