from requests import post
url = "https://api.snapp.ir/api/v1/sms/link"
data = {
    "phone": "09050756226"
}

res = post(url=url, data=data)
print(res)