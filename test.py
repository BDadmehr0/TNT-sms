from requests import post

link = 'https://api.lendo.ir/api/customer/auth/send-otp'
data = {
    "mobile":"09050756226"
}

# 	https://api.lendo.ir/api/customer/auth/send-otp

print(post(url=link, data=data))

