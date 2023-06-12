from requests import post

link = 'https://www.buskool.com/send_verification_code'
data = {
    "phone":"09050756226"
}

print(post(url=link, data=data))

