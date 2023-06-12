from requests import post

link = 'https://api.lendo.ir/api/customer/auth/send-otp'
data = {
    "mobile":"09050756226"
}

print(post(url=link, data=data))

