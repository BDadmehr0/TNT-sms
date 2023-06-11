from requests import post

link = 'https://www.sheypoor.com/api/v10.0.0/auth/send'
data = {
    "username": "09050756226"
}

print(post(url=link, data=data))