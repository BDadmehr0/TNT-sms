from requests import post

link = 'https://mobapi.banimode.com/api/v2/auth/request'
data = {
    "phone":"09050756226"
}

print(post(url=link, data=data))