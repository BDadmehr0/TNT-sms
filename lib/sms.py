# Dadmehr - Garfox
# packages
import requests
import random
from fake_useragent import UserAgent
import json

# +_+_+_+ User Agent Genrator +_+_+_+
# ua = UserAgent()
# user = ua.random
# print(user)


range_n_limet = 100

def send(phone_number,range_n): # add prvity Change IP
    pass

with open('./API/sms.json') as json_file:
    data = json.load(json_file)

url_data = data['filimo']

url = url_data['url']
data = url_data['data']

print(data, url)

s = requests.Session()
res = s.post(url, data)

print(res)