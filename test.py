from requests import post
url = "https://app.sms.ir/auth/sign-up?mobile=09050756226"
data = {
    "mobile": "09050756226"
}

res = post(url=url, data=data)
print(res)